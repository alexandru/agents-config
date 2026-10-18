# Share skill sources without vendoring

Install shared skills globally from the same sources rather than vendoring copies into harness repositories, so their content does not fork between harnesses. Each harness provides standalone installation into the shared user skill directory; harness-specific adapters remain tracked with their harness configuration.

Capability substitutes are allowed when harness support differs. Copilot installs `mcp-access` because the work Copilot environment disables native MCP support; the skill restores access rather than introducing a different intended capability.
