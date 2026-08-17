# Agents' Config

## Repository scope

- This repository maintains configurations for OpenCode, Copilot CLI, and Pi.
- Treat `SPEC.md` as the central specification for behavior shared across harnesses.
- Keep `SPEC.md` short and high-level. Describe required behavior and boundaries, not prompt wording.
- Keep shared agents, prompts, skills, commands, and behavior aligned across `opencode/`, `copilot/`, and `pi/`.
- Allow harness-specific differences only where required by tool names, permission or configuration syntax, cache paths, model names, or invocation mechanisms.
- Treat `pi/AGENTS.md` as Pi's Orchestrator prompt. Keep it semantically aligned with `opencode/agents/Orchestrator.md` and `copilot/agents/Orchestrator.agent.md`.

## Git rules

- `opencode/`, `copilot/`, and `pi/` are Git submodules.
- Run Git commands for submodule files from the corresponding submodule working tree, for example `git -C opencode status`.
- Check status and diffs in the parent repository and all three submodules.
- Never commit or push changes. Leave all work uncommitted for review.

## Shared-change checklist

- For every shared configuration change:
  - Update `SPEC.md` so it remains the source of truth.
  - Apply the change to every applicable harness.
  - Update every affected README and user-facing list.
  - Verify semantic alignment across all harnesses after accounting for allowed harness-specific differences.
- When adding or updating a shared skill:
  - Add it to the official shared skill list in `SPEC.md`.
  - Install it in each harness with `npx skills add <source> -y --skill <name>` rather than copying files manually.
  - Add the same `npx skills add` command to each harness's `update-skills` target in its `Makefile`.
  - Ensure each harness's `skills-lock.json` is updated by the installer.
  - Update the skill lists in all harness READMEs.
  - Review the vendored skill files and all resulting diffs.
- When changing a shared agent prompt:
  - Update the corresponding behavior in `SPEC.md`.
  - Summarize behavior in `SPEC.md`; do not copy exact prompt text into it.
  - Apply the same semantics to OpenCode, Copilot CLI, and Pi.
  - Preserve deliberate user-authored phrasing unless the user asks for a rewrite.
  - Preserve only differences required by each harness's capabilities or file format.
