# Provide Orchestrator and Junior as a user-invoked skill

Provide `orchestrate` in the skills submodule for sessions where the user cannot configure the agents. The skill preserves the role boundaries and delegation rules so users can reduce cost and context use while Orchestrator handles decisions and verifies the work. The existing harness configurations stay in place.

Use the Codex role prompts as the wording reference for the skill because Codex is its primary use case. Keep the skill wording in sync with those prompts and limit changes to skill invocation, delegation, model selection, and harness capabilities. OpenCode remains the source of truth for harness alignment.

Activate the skill only on explicit user invocation. Ask the user which model Junior should use if the user did not specify one. Run Junior on the selected model and give each new Junior its role prompt and a self-contained assignment. Start each visible delegated task or session name with the role so users can identify who does the work.
