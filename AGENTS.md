# Agents' Config

## Repository scope

- This repository maintains configurations for OpenCode, Copilot CLI, and Codex.
- Treat `SPEC.md` as the central specification for behavior shared across harnesses.
- Keep `SPEC.md` short and high-level. Describe required behavior and boundaries, not prompt wording.
- Keep shared agents, prompts, skills, commands, and behavior aligned across `opencode/`, `copilot/`, and `codex/`.
- Allow harness-specific differences only where required by tool names, permission or configuration syntax, cache paths, model names, or invocation mechanisms.
- Do not repeat restrictions in agent prompts when the harness enforces them natively.

## Git rules

- `opencode/`, `copilot/`, and `codex/` are Git submodules.
- Run Git commands for submodule files from the corresponding submodule working tree, for example `git -C opencode status`.
- Check status and diffs in the parent repository and all submodules.
- Never commit or push changes. Leave all work uncommitted for review.

## Repository invariants

- `SPEC.md` is the source of truth for shared behavior. Shared sections must remain harness-neutral; operational details belong in harness configuration or its README.
- Every harness has the same configured agent roster, role boundaries, delegation graph, and shared skills unless `SPEC.md` explicitly says otherwise.
- Shared agent prompts must preserve the same semantics. Differences are limited to native tool names, permissions, paths, models, file formats, and invocation mechanisms.
- Enforce restrictions natively when supported. Use prompt restrictions only where native enforcement is unavailable.
- Harness READMEs must use the same shared agent and skill names, ordering, and descriptions. Skills must be grouped under links to the sources used by each Makefile's `update-skills` task. Installation, commands, profiles, and invocation may differ by harness.
- Shared skills must come from the same source and be installed with `npx skills add`, never copied manually. Each harness must track matching installer commands, lock entries, and vendored skill content.
- Every installed user-invoked OpenCode skill must have a command wrapper that invokes the skill, plus matching `SPEC.md` and README entries.
- Root documentation, Makefiles, Git helpers, and `.gitmodules` must include every harness submodule.
- Source configuration must remain tracked. Generated files, credentials, sessions, logs, caches, and other runtime state must remain ignored.
- Removed agents, skills, commands, and settings must leave no stale source or generated configuration references.

## Change checklist

- [ ] Update `SPEC.md` for every shared behavior change without adding harness implementation details to shared sections.
- [ ] Apply shared agent changes to every harness and preserve deliberate user-authored phrasing.
- [ ] Update every affected README and user-facing list.
- [ ] For shared skills, update `SPEC.md`, every harness Makefile, every `skills-lock.json`, vendored files, and every README source group and skill list.
- [ ] Install skills with the recorded `npx skills add <source> -y --skill <name>` command and review all resulting diffs.
- [ ] Search all harnesses and generated local configuration for stale names and removed settings.
- [ ] Compare agent permissions and prompts against `SPEC.md`, accounting only for required harness differences.

## Periodic audit

- Run the full change checklist before handing work off, before every configuration release, after harness CLI or skill-installer upgrades, and at least monthly while the repository is actively maintained.
- During the audit, compare all harness rosters, prompts, permissions, skills, READMEs, Makefiles, lock files, ignore rules, and root integration files.
- Record or fix every drift. Do not silently preserve accidental differences.
