.PHONY: update-skills

update-skills:
	$(MAKE) -C opencode update-skills
	$(MAKE) -C copilot update-skills
	$(MAKE) -C codex update-skills
