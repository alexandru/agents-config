# Give every harness native web search

Each harness reaches web search through its native mechanism: OpenCode through its `websearch.provider: brave` plugin, Copilot CLI and Codex through the `web_search` tools bundled with their subscriptions, Claude Code through its built-in `WebSearch` tool, and Pi — which has no built-in web search tool — through the Brave Search MCP server in `harnesses/pi/mcp.json`, with `exposure: direct` and the environment's `BRAVE_SEARCH_API_KEY` bridged to the server's `BRAVE_API_KEY`.

Because native search exists everywhere, the shared Brave `web-search` skill is in no harness's skill roster; Copilot CLI, Codex, and Claude Code rely on their built-in tools, matching the OpenCode baseline.
