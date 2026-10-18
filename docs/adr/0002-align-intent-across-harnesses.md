# Align intent across harnesses

Align intended behavior rather than configuration syntax because harnesses expose different tools, permissions, and agent systems. Prefer native enforcement, then prompt instructions where native enforcement is unavailable; do not weaken the source of truth to the lowest common denominator.

Harness-specific plugins, skills, and other mechanisms may provide equivalent capabilities without individual ADRs. Record intentional behavioral exceptions in ADRs, and ask when it is unclear whether a difference is a capability adaptation or an exception.

OpenCode's directory-access allowlists are harness-specific, not restrictions to reproduce in Copilot or Codex. They are fragile when shell access can bypass them; OpenCode's shell-safety plugin can strengthen enforcement, but this mechanism is not a portable requirement.
