#!/usr/bin/env python3

"""Regression tests for bin/git-checkout. Run: python3 tests/git-checkout-test.py

Each test clones a scratch parent repository whose target branch omits one
submodule, mirroring a parent branch that does not track every entry in the
helper's hard-coded submodule list.
"""

import os
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

SOURCE_ROOT = Path(__file__).resolve().parent.parent
HELPER = SOURCE_ROOT / "bin" / "git-checkout"

SUBMODULES = (
    "opencode",
    "copilot",
    "codex",
    "pi",
    "claude",
    "skills",
    "plugins/opencode-shell-safety",
    "plugins/opencode-brave-search",
    "plugins/opencode-session-todo",
)
ORIGIN_NAMES = {
    "opencode": "opencode",
    "copilot": "copilot",
    "codex": "codex",
    "pi": "pi",
    "claude": "claude",
    "skills": "skills",
    "plugins/opencode-shell-safety": "opencode-shell-safety",
    "plugins/opencode-brave-search": "opencode-brave-search",
    "plugins/opencode-session-todo": "opencode-session-todo",
}

ENV = os.environ.copy()
ENV.update(
    {
        "GIT_AUTHOR_NAME": "test",
        "GIT_AUTHOR_EMAIL": "test@example.invalid",
        "GIT_COMMITTER_NAME": "test",
        "GIT_COMMITTER_EMAIL": "test@example.invalid",
        "GIT_CONFIG_COUNT": "1",
        "GIT_CONFIG_KEY_0": "protocol.file.allow",
        "GIT_CONFIG_VALUE_0": "always",
    }
)


def git(*args: str, cwd: Path | None = None, check: bool = True) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ("git", *args),
        cwd=cwd,
        env=ENV,
        text=True,
        capture_output=True,
        check=False,
    )
    if check and result.returncode != 0:
        raise AssertionError(
            f"git {' '.join(args)} failed in {cwd or Path.cwd()}:\n{result.stderr}"
        )
    return result


class GitCheckoutTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.temp = tempfile.TemporaryDirectory(prefix="git-checkout-test-")
        cls.addClassCleanup(cls.temp.cleanup)
        cls.base = Path(cls.temp.name)
        origins = cls.base / "origins"
        seeds = cls.base / "seeds"
        origins.mkdir()
        seeds.mkdir()

        for path in SUBMODULES:
            name = ORIGIN_NAMES[path]
            seed = seeds / name
            git("init", "-q", str(seed))
            git("checkout", "-q", "-b", "main", cwd=seed)
            (seed / "README.md").write_text(f"{name} main\n", encoding="utf-8")
            git("add", "README.md", cwd=seed)
            git("commit", "-qm", f"init {name}", cwd=seed)
            git("branch", "legacy", cwd=seed)
            origin = origins / f"{name}.git"
            git("init", "-q", "--bare", str(origin))
            git("remote", "add", "origin", str(origin), cwd=seed)
            git("push", "-q", "origin", "main", "legacy", cwd=seed)
            git("symbolic-ref", "HEAD", "refs/heads/main", cwd=origin)

        root = cls.base / "root"
        git("init", "-q", str(root))
        git("checkout", "-q", "-b", "main", cwd=root)
        (root / "README.md").write_text("root main\n", encoding="utf-8")
        git("add", "README.md", cwd=root)
        git("commit", "-qm", "root with nine submodules", cwd=root)
        for path in SUBMODULES:
            origin = origins / f"{ORIGIN_NAMES[path]}.git"
            git(
                "submodule",
                "add",
                "-q",
                "-b",
                "main",
                origin.as_uri(),
                path,
                cwd=root,
            )
        git("add", ".gitmodules", cwd=root)
        git("commit", "-qm", "record nine submodules", cwd=root)

        git("checkout", "-q", "-b", "legacy", cwd=root)
        git("rm", "-q", "--cached", "claude", cwd=root)
        git("config", "-f", ".gitmodules", "--remove-section", "submodule.claude", cwd=root)
        git("add", ".gitmodules", cwd=root)
        git("commit", "-qm", "legacy without claude", cwd=root)

        cls.root_origin = origins / "root.git"
        git("init", "-q", "--bare", str(cls.root_origin))
        git("remote", "add", "origin", str(cls.root_origin), cwd=root)
        git("push", "-q", "origin", "main", "legacy", cwd=root)
        git("symbolic-ref", "HEAD", "refs/heads/main", cwd=cls.root_origin)

    def make_clone(self, name: str, branch: str) -> Path:
        clone = self.base / "work" / name
        clone.parent.mkdir(parents=True, exist_ok=True)
        git(
            "clone",
            "-q",
            "--branch",
            branch,
            self.root_origin.as_uri(),
            str(clone),
        )
        bin_dir = clone / "bin"
        bin_dir.mkdir()
        shutil.copy2(HELPER, bin_dir / "git-checkout")
        (bin_dir / "git-checkout").chmod(0o755)
        return clone

    def run_helper(self, clone: Path, branch: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            (str(clone / "bin" / "git-checkout"), branch),
            cwd=clone,
            env=ENV,
            text=True,
            capture_output=True,
            check=False,
            timeout=120,
        )

    def assert_checked_out(self, clone: Path, paths: tuple[str, ...], branch: str) -> None:
        for path in paths:
            with self.subTest(submodule=path):
                self.assertTrue((clone / path).is_dir(), path)
                result = git("branch", "--show-current", cwd=clone / path)
                self.assertEqual(result.stdout.strip(), branch, path)

    def test_present_submodules_continue_through_skills_and_plugins(self) -> None:
        clone = self.make_clone("present", "main")

        result = self.run_helper(clone, "main")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("fatal:", result.stderr)
        self.assert_checked_out(clone, SUBMODULES, "main")

    def test_absent_target_submodule_with_absent_directory_is_skipped(self) -> None:
        clone = self.make_clone("absent", "main")

        result = self.run_helper(clone, "legacy")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("fatal:", result.stderr)
        self.assertFalse((clone / "claude").exists())
        self.assert_checked_out(
            clone, tuple(path for path in SUBMODULES if path != "claude"), "legacy"
        )

    def test_absent_target_submodule_with_leftover_directory_is_skipped(self) -> None:
        clone = self.make_clone("leftover", "legacy")
        leftover = clone / "claude"
        leftover.mkdir()
        (leftover / "leftover.txt").write_text("leftover\n", encoding="utf-8")
        (leftover / ".git").write_text(
            "gitdir: ../.git/modules/claude\n", encoding="utf-8"
        )
        tracked = git(
            "ls-files", "--error-unmatch", "--", "claude", cwd=clone, check=False
        )
        self.assertNotEqual(tracked.returncode, 0, tracked.stdout)

        result = self.run_helper(clone, "legacy")

        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertNotIn("fatal:", result.stderr)
        self.assertEqual(
            (leftover / "leftover.txt").read_text(encoding="utf-8"), "leftover\n"
        )
        self.assertEqual(
            (leftover / ".git").read_text(encoding="utf-8"),
            "gitdir: ../.git/modules/claude\n",
        )
        self.assert_checked_out(
            clone, tuple(path for path in SUBMODULES if path != "claude"), "legacy"
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
