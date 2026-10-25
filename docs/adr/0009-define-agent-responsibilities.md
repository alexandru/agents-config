# Define agent responsibilities

Orchestrator is a main agent only, never a delegation target. It owns implementation decisions and integration.

Solo works directly. Delegation is optional and limited to other Solo instances, preserving its independence from specialist agents. Other agents must not delegate to Solo.

Invoke Analyst when the user requests fresh-eyes code analysis. Analyst is a read-only advisor and the only specialist sub-agent permitted to judge code: exercising independent judgment is its purpose, not merely gathering evidence for Orchestrator.

Explorer and Librarian gather factual evidence without judging code, diagnosing bugs, or recommending solutions. Junior handles specified execution. These boundaries keep evidence gathering and execution separate from judgment without preventing user-requested independent analysis.
