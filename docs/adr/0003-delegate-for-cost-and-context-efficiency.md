# Delegate for cost and context efficiency

Delegate bounded grunt work to cheaper models to reduce total cost while preserving quality. Keep Orchestrator long-lived and protect its context from tool-heavy work so it stays compaction-free and effective for longer; work directly when delegation overhead outweighs the benefit.

Only Orchestrator may receive delegated work requiring judgment. It may recursively invoke another Orchestrator when instructions require parallelism for work specialists cannot perform, or when workflow instructions require independent judgment. Keep independent-review handoffs untainted by the caller's prior reasoning. Delegation is not exclusively a way to use cheaper models.
