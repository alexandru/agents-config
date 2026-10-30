# Agents Config

This repository unifies several projects as git submodules:

- Harness configurations:
    - [opencode](https://github.com/alexandru/opencode-config)
    - [copilot](https://github.com/alexandru/copilot-config)
    - [codex](https://github.com/alexandru/codex-config)
    - [codex-cloud](https://github.com/alexandru/codex-cloud-config)
    - [pi](https://github.com/alexandru/pi-config)
    - [claude](https://github.com/alexandru/claude-config)
- Plugins:
    - [opencode-brave-search](https://github.com/alexandru/opencode-brave-search) ([npm](https://www.npmjs.com/package/opencode-brave-websearch))

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
