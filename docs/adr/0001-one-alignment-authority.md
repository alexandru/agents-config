# One alignment authority

Use one harness configuration as the source of truth for alignment so parallel implementations do not become competing definitions of intended behavior. Name the current source of truth in `AGENTS.md`, where it can change without rewriting this decision; the user's prompt may override it. Alignment follows that authority rather than silently redesigning its behavior.
