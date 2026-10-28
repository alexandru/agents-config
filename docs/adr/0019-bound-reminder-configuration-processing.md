# Bound reminder configuration processing

Copilot reminders impose a structural nesting limit before fully parsing configuration, rather than accepting unrestricted condition nesting. A resource-exhaustion failure in a pre-tool hook can block agent work, so excessive configuration must instead produce a non-blocking diagnostic. Keep the concrete limit in the utility's configuration contract and help output.
