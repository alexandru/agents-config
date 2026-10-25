# Define agent responsibilities

Orchestrator owns judgment: diagnosis, design, trade-offs, code review, implementation decisions, and integration. It has full tool access and works directly or delegates. It is both a main agent and a delegation target, so instructions that require independent judgment, such as fresh-eyes reviews, are served without a separate reviewer role.

Solo works directly. Delegation is optional and limited to other Solo instances, preserving its independence from specialist agents. Other agents must not delegate to Solo.

Junior gathers local and external evidence and executes specified work. It does not plan, diagnose, review, or judge correctness, beyond obvious fixes such as those following from compiler output, and it does not delegate.

Merging evidence gathering and execution into Junior, and dropping read-only specialists and a read-only reviewer, trades native read-only enforcement for a smaller roster that is simpler to delegate to.
