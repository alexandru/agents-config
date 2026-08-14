# Agents Config

All of my agents' config in one place. This repo unifies the following:

- [alexandru/opencode-config](https://github.com/alexandru/opencode-config)
- [alexandru/copilot-cli-config](https://github.com/alexandru/copilot-cli-config)

## Working with the repo

Clone with submodules:

```bash
git clone --recurse-submodules git@github.com:alexandru/copilot-cli-config.git
```

If you already cloned the repository:

```bash
git submodule update --init --recursive
```

Each submodule is its own repository.

1. Edit files inside `opencode/` or `copilot/`.
2. Commit and push inside that submodule.
3. Return to the repository root and stage the updated submodule pointers:

```bash
git add opencode copilot
git commit -m "Update submodule pointers"
git push
```
