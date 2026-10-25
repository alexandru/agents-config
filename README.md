# Agents Config

This repository unifies several projects as git submodules:

- Harness configurations:
    - [opencode](https://github.com/alexandru/opencode-config)
    - [copilot](https://github.com/alexandru/copilot-config)
    - [codex](https://github.com/alexandru/codex-config)
    - [pi](https://github.com/alexandru/pi-config)
    - [claude](https://github.com/alexandru/claude-config)
- Plugins:
    - [opencode-shell-safety](https://github.com/alexandru/opencode-shell-safety) ([npm](https://www.npmjs.com/package/opencode-shell-safety))
    - [opencode-brave-search](https://github.com/alexandru/opencode-brave-search) ([npm](https://www.npmjs.com/package/opencode-brave-websearch))
    - [opencode-session-todo](https://github.com/alexandru/opencode-session-todo) ([npm](https://www.npmjs.com/package/opencode-session-todo))

- [Skills](https://github.com/alexandru/skills)

## Working with the repo

Clone with submodules:

```bash
git clone --recurse-submodules git@github.com:alexandru/agents-config.git
```

If you already cloned the repository:

```bash
git submodule update --init --recursive
```
