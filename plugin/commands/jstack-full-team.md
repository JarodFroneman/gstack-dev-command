# /jstack-full-team

Run JStack with the full 11-role engineering team.

## Arguments

- `goal`: the task or project objective to execute.

## Workflow

1. Treat this command as explicit user approval to deploy the full JStack team when multi-agent tools are available.
2. Use the full roster: Lead Engineer, Architect, Code Investigator, Builder, Reviewer, QA Engineer, Security Engineer, DevOps / Release Engineer, Product / UX Reviewer, Quant / Backtest Reviewer, and Documentation / Handoff Writer.
3. Keep the Lead Engineer accountable for scope, synthesis, final implementation decisions, verification, and user handoff.
4. Keep specialists read-only by default.
5. Allow Builder to edit implementation files only inside an explicitly assigned disjoint write scope.
6. Allow Documentation / Handoff Writer to edit docs only when assigned.
7. Use `jstack_team_plan` and `jstack_dispatch_check` when available.

## Guardrails

If platform concurrency limits prevent all specialists from running at once, dispatch them in waves while preserving the full-team evidence contract. If multi-agent tools are unavailable, write `No subagents deployed:` with the concrete reason, then continue with the single-lead enterprise workflow while manually applying the full-team review rubric.
