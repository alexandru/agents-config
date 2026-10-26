# Keep todo handling harness-specific

Each harness tracks todos with its native todo tool, and those tools differ in how lists are scoped and shown to the user. Todo handling is therefore not aligned across harnesses: no agent is denied todo tracking for alignment's sake, and differences in todo tools or todo-specific prompt sections do not count as drift.
