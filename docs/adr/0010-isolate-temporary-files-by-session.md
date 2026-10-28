# Isolate temporary files by session

Keep temporary files under each harness's temporary directory, isolated by the agent's own session ID to avoid conflicts. Do not pass session directories in delegation handoffs; exchange specific file paths when needed.

Keep the persistent research cache of the `external-research` skill shared across sessions and harnesses, separate from session scratch. Authorize these directories narrowly and keep shared skills read-only through native controls where available; do not substitute prompt restrictions for filesystem enforcement.
