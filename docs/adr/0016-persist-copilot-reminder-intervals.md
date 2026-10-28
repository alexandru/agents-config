# Persist Copilot reminder intervals across restarts

Copilot reminder intervals survive command-hook process exits and session resumes, unlike the in-memory OpenCode plugin. Store each session's active agent policy and intervals together, serializing updates across processes; a changed agent or effective policy starts fresh intervals. This keeps stateless hook invocations meaningful and prevents restarting the CLI from discarding accumulated reminders, without preserving an earlier agent's intervals when switching back to it.
