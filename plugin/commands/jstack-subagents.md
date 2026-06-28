# /jstack-subagents

Run JStack with the right specialist subagent team for the current task.

## Arguments

- `goal`: the task or project objective to execute.

## Workflow

1. Treat this command as explicit user approval to deploy subagents when multi-agent tools are available.
2. Use the Lead Engineer plus the right specialist team, normally two or three specialists.
3. For normal feature or bug work, use Code Investigator plus Reviewer.
4. For phase, milestone, or project work, use Code Investigator plus Reviewer, adding QA when verification risk is meaningful.
5. For architecture, API, database, or integration work, use Architect, Code Investigator, and Reviewer.
6. For UI/product work, use Product / UX Reviewer, QA Engineer, and Reviewer.
7. For security/compliance work, use Security Engineer, Reviewer, and QA Engineer.
8. For production/release/deploy work, use DevOps / Release Engineer, Security Engineer, and QA Engineer.
9. For trading, EA, quant, or backtest work, use Quant / Backtest Reviewer, Reviewer, and QA Engineer.
10. Use `jstack_team_plan` and `jstack_dispatch_check` when available before spawning several specialists or assigning file edits.

## Guardrails

Specialists are read-only by default. Only a Builder may edit, and only inside an explicitly assigned disjoint write scope. If multi-agent tools are unavailable, write `No subagents deployed:` with the concrete reason, then continue with the single-lead enterprise workflow.
