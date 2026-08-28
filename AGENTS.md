# Agents' Config

## Repository scope

- Configures OpenCode, Copilot CLI, and Codex.
- `skills/` contains custom skills shared across the agent configurations,
  including `simplify`. Keep these separate from installed third-party skills.
- `SPEC.md` governs shared behavior.
- Keep `SPEC.md` short and high-level: behavior and boundaries, not prompt wording.
- Align shared agents, prompts, skills, commands, and behavior across `opencode/`, `copilot/`, and `codex/`.
- Limit harness differences to required tool names, permissions, configuration syntax, cache paths, models, and invocation mechanisms.
- Do not restate natively enforced restrictions in prompts.
- Never edit a README without explicit user approval unless the edit is required to fix an invalid or broken reference.

## Git rules

- `opencode/`, `copilot/`, and `codex/` are Git submodules.
- Run submodule Git commands from its worktree, for example `git -C opencode status`.
- Check parent and all submodule statuses and diffs.
- Never commit or push; leave changes uncommitted for review.

## Repository invariants

- Keep shared `SPEC.md` sections harness-neutral; put operational details in harness configuration or README.
- Unless `SPEC.md` says otherwise, every harness has the same agent roster, role boundaries, delegation graph, and shared skills.
- Preserve prompt semantics; vary only native tool names, permissions, paths, models, formats, and invocation mechanisms.
- Enforce restrictions natively when possible; use prompts otherwise.
- Keep shared agent and skill names, order, and descriptions identical across harness READMEs. Group skills under links to sources used by Makefile installation targets. Only installation, commands, profiles, and invocation may differ.
- Source shared third-party skills identically and install them globally with `npx skills add`; never copy or vendor them. Each harness must track matching installers targeting the shared user skill directory. Do not track project-local skill locks.
- Track harness-authored, harness-specific skills as source configuration; exclude them from the shared third-party roster.
- Give every installed user-invoked OpenCode skill a command wrapper and matching `SPEC.md` and README entries.
- Root documentation, Makefiles, Git helpers, and `.gitmodules` must include every harness submodule.
- Track source configuration; ignore generated files, credentials, sessions, logs, caches, and other runtime state.
- Remove all source and generated references to removed agents, skills, commands, and settings.

## Change checklist

- [ ] For shared behavior changes, update `SPEC.md` without harness details.
- [ ] Apply shared agent changes to every harness; preserve deliberate user wording.
- [ ] Update affected READMEs and user-facing lists.
- [ ] For shared skills, update `SPEC.md`, every harness Makefile, and every README source group and skill list.
- [ ] Run recorded `npx skills add <source> -g -a <agent> -y --skill <name>` commands; review installed content before use.
- [ ] Search all harnesses and generated local configuration for stale names and removed settings.
- [ ] Compare agent permissions and prompts with `SPEC.md`; allow only required harness differences.

## Periodic audit

- Run the full checklist before handoff or release, after harness CLI or skill-installer upgrades, and monthly while active.
- Compare all harness rosters, prompts, permissions, shared skill installers, harness-authored skills, READMEs, Makefiles, ignore rules, and root integration files.
- Record or fix all drift; never preserve accidental differences.
