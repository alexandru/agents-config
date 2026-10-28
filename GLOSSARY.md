# Agents' Config

Shared language for aligning agent harness configurations.

## Language

**Harness**:
A program that runs an agent loop and supplies its tools, permissions, sub-agents, and skills, such as OpenCode, Copilot CLI, Codex, Pi, or Claude Code.
_Avoid_: agent system, tool, client

**Harness configuration**:
The configuration that sets up one harness, including its agents, permissions, skills, and settings.

**Agent**:
A configured role within a harness, defined by its prompt, permissions, and delegation targets.

**Alignment**:
Equivalent intended behavior across harnesses, adapted to their different capabilities rather than expressed through identical configuration.

**Source of truth**:
The harness configuration that serves as the default authority when aligning the other harnesses.

**Orchestrator**:
The judgment-owning agent: it diagnoses, designs, decides, and integrates, works directly when that is cheapest, and delegates to Junior or to other Orchestrators.
_Avoid_: Senior

**Solo**:
The independent agent: it exercises judgment and works directly, without delegating to Junior.

**Junior**:
The execution and evidence agent: it gathers local and external evidence and carries out specified work, without owning judgment or delegating.
_Avoid_: Explorer, Librarian

**Agent reminder**:
A non-blocking instruction that recalls an agent's prompt obligations while leaving judgment and action selection with that agent.

**Reminder interval**:
The span over which one reminder rule accumulates measurements and observed events, beginning anew when that rule resets.

**Event condition**:
A reminder condition satisfied when its named event has occurred during the current reminder interval.
