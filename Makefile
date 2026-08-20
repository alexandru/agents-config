.PHONY: install-skills update-skills

# Shared skills use one cross-harness global installation. Every standalone
# harness exposes the same targets; invoking one is sufficient from this repo.
install-skills:
	$(MAKE) -C opencode install-skills

update-skills:
	$(MAKE) -C opencode update-skills
