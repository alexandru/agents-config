# Agents' Config

## Repository scope

- Configures OpenCode, Copilot CLI, and Codex.
- `codex/AGENTS.md` is a delivered artifact: the main-agent prompt shipped by that sub-project, not guidelines for developing it. Treat it as source configuration; this root `AGENTS.md` governs development of that sub-project.
- `skills/` contains custom 1st party skills shared across the agent configurations.
- `opencode/` is the source of truth for harness alignment unless the user's prompt specifies otherwise.
- Architectural decisions and intentional alignment exceptions live in `docs/adr/`.
- Align shared agents, prompts, skills, commands, and behavior across `opencode/`, `copilot/`, and `codex/`.
- Preserve intent across harnesses; adapt to their capabilities rather than requiring identical configuration.
- Do not restate natively enforced restrictions in prompts.
- Never edit a README without explicit user approval unless the edit is required to fix an invalid or broken reference.

## Git rules

- `opencode/`, `copilot/`, and `codex/` are Git submodules.
- Run submodule Git commands from its worktree, for example `git -C opencode status`.
- Check parent and all submodule statuses and diffs.
- Never commit or push; leave changes uncommitted for review.

## Repository invariants

- Keep ADRs focused on intent, decisions, and rationale; leave implementation details in harness configuration.
- Align agent rosters, role boundaries, delegation, and shared skills with the source of truth unless an ADR records an exception.
- Preserve prompt semantics using each harness's available features; record intentional behavioral exceptions in ADRs.
- Enforce restrictions natively when possible; use prompts otherwise.
- Keep shared agent and skill names, order, and descriptions identical across harness READMEs. Group skills under links to sources used by Makefile installation targets. Only installation, commands, profiles, and invocation may differ.
- Source shared skills identically and install them globally with `npx skills add`; never copy or vendor them into harness repositories. Each harness must track matching installers targeting the shared user skill directory. Do not track project-local skill locks.
- Track harness-authored, harness-specific skills as source configuration; exclude them from the shared third-party roster.
- Give every installed user-invoked OpenCode skill a command wrapper and matching README entry.
- Root documentation, Makefiles, Git helpers, and `.gitmodules` must include every harness submodule.
- Track source configuration; ignore generated files, credentials, sessions, logs, caches, and other runtime state.
- Remove all source and generated references to removed agents, skills, commands, and settings.
- Harness `bin/` scripts with logic are single-file Python: pinned dependencies in PEP 723 inline metadata, run via `pipx run`, invoked through a symlink, statically typed and `mypy --strict` clean.
- Expected failures in Python `bin/` scripts raise one clear domain error; users never see a traceback.

## Change checklist

- [ ] For architectural decisions or intentional alignment exceptions, update the relevant ADRs.
- [ ] Apply shared agent changes to every harness; preserve deliberate user wording.
- [ ] Update affected READMEs and user-facing lists.
- [ ] For shared skills, update every harness Makefile and every README source group and skill list.
- [ ] Run recorded `npx skills add <source> -g -a <agent> -y --skill <name>` commands; review installed content before use.
- [ ] Search all harnesses and generated local configuration for stale names and removed settings.
- [ ] Compare harness configurations with the source of truth and relevant ADRs; distinguish capability adaptations from behavioral exceptions.

## Periodic audit

- Run the full checklist before handoff or release, after harness CLI or skill-installer upgrades, and monthly while active.
- Compare all harness rosters, prompts, permissions, shared skill installers, harness-authored skills, READMEs, Makefiles, ignore rules, and root integration files.
- Record or fix all drift; never preserve accidental differences.

## Agent skills

### Issue tracker

Issues are tracked in GitHub Issues via the `gh` CLI. See `docs/agents/issue-tracker.md`.

### Domain docs

Single-context: a root `GLOSSARY.md` and `docs/adr/`. See `docs/agents/domain.md`.
