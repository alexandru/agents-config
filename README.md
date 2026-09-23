# Agents Config

All of my agents' config in one place. This repo unifies the following:

- [opencode-config](https://github.com/alexandru/opencode-config)
- [copilot-config](https://github.com/alexandru/copilot-config)
- [codex-config](https://github.com/alexandru/codex-config)
- [pi-config](https://github.com/alexandru/pi-config)
- [skills](https://github.com/alexandru/skills)
- [plugins/opencode-shell-safety](https://github.com/alexandru/opencode-shell-safety)

The `skills` repository contains my custom skills shared across the agent
configurations.

## Working with the repo

Clone with submodules:

```bash
git clone --recurse-submodules git@github.com:alexandru/agents-config.git
```

If you already cloned the repository:

```bash
git submodule update --init --recursive
```

Six submodules are included; each is its own repository.

Shared custom and third-party skills are installed once for all harnesses under
`~/.agents/skills`:

```bash
make install-skills
```

To reinstall them from their configured upstream sources and check the pinned
Matt Pocock skill release:

```bash
make update-skills
```

The root scripts apply the Git workflow to all submodules and then the parent repository:

```bash
./bin/git-add
./bin/git-commit "Commit message"
./bin/git-push
```
