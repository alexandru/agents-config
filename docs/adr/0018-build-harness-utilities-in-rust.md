# Build harness utilities in Rust

Harness utilities use standalone Cargo workspaces, with one crate per utility. Harness Makefiles build release executables into their binary directories instead of tracking platform-specific binaries. This provides typed, testable utilities without an interpreter on each invocation; installation consequently requires a Rust toolchain. Migrate all existing Python-based utilities incrementally using this model.
