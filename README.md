# Agents Config

All of my agents' config in one place. This repo unifies the following:

- [opencode-config](https://github.com/alexandru/opencode-config)
- [copilot-cli-config](https://github.com/alexandru/copilot-cli-config)
- [Pi configuration](./pi/)

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

The root scripts apply the Git workflow to both submodules and then the parent repository:

```bash
./bin/git-add
./bin/git-commit "Commit message"
./bin/git-push
```
