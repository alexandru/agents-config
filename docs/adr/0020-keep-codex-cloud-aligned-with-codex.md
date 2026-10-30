# Keep Codex Cloud aligned with Codex

Keep `harnesses/codex-cloud/` aligned with `harnesses/codex/` for main-agent instructions, agent roster and prompts, models and reasoning settings, permissions, tools, features, and shared engineering behavior. Review changes to the main Codex configuration and carry them across, subject to the skill-distribution exceptions below.

Track ready-to-use native configuration and agent files instead of requiring local generators, custom scripts, or the local bootstrap and deployment procedure. Cloud has one configuration, matching the effective default settings of the main Codex configuration. Its README provides concise environment setup instructions.

Declare `alexandru-skills@alexandru` and `mattpocock-skills@mattpocock` as native Codex plugins in `config.toml`, using their Git marketplaces without pinned refs. Refresh the marketplaces through the Codex CLI during Cloud environment setup to install and enable the latest complete plugin bundles. Cloud intentionally accepts their full skill rosters rather than reproducing the main configuration's selected skills. Native plugin installation replaces the Makefile and `npx skills` dependency; the main Codex configuration keeps its existing installer.

Native plugin storage and skill namespacing, complete bundles, unpinned versions, installation, and concise documentation are intentional exceptions to shared harness alignment. These exceptions do not permit dropping agents, weakening delegation requirements, or omitting configuration because Cloud support is unconfirmed. Record any verified Cloud incompatibility explicitly, with the smallest necessary adaptation, rather than treating missing documentation as evidence that a capability is unsupported.
