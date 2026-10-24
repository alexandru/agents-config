# Restrict Orchestrator tool access

Restrict the Orchestrator's tool access unconditionally: it works on files directly and delegates command execution, research, and evidence gathering to specialists, instead of running shell commands or using web or MCP tools itself. The boundary is not conditioned on how reliably the harness or the model delegates.

Enforce it by whatever means necessary: natively where the harness scopes tools per agent, in the prompt where it cannot.

Codex can disable a named agent's shell natively but cannot scope web or MCP tools per agent, and its main agent has no per-agent configuration; its Orchestrator restriction is prompt-enforced.

Pi enforces the shell boundary natively and its MCP and web boundary in the prompt, since directly exposed MCP tools cannot be hidden from the main agent.
