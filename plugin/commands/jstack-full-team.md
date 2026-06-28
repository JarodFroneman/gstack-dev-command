---
description: Run JStack with the full 11-role engineering team
argument-hint: [GOAL]
---

Apply the custom JStack enterprise development workflow to this task.

Goal:
$ARGUMENTS

Mode: `full-team`.

The user invoked `/jstack-full-team`, which is explicit approval to deploy the
full JStack specialist team when multi-agent tools are available.

Use the full 11-role roster:

1. Lead Engineer
2. Architect
3. Code Investigator
4. Builder
5. Reviewer
6. QA Engineer
7. Security Engineer
8. DevOps / Release Engineer
9. Product / UX Reviewer
10. Quant / Backtest Reviewer
11. Documentation / Handoff Writer

The Lead Engineer remains accountable. Specialists are read-only by default.
Builder is the only specialist that may edit implementation files, and only with
an explicitly assigned disjoint write scope. Documentation / Handoff Writer may
edit docs only when assigned.

If platform concurrency limits prevent all specialists from running at once,
dispatch them in waves while preserving the full-team evidence contract.

Full team means complete professional coverage, not uncontrolled concurrency.
Before dispatching, create a coordination packet with:

- goal
- risk class
- roles used and why
- read/write permissions
- file ownership map
- evidence contract
- conflict rule
- stop conditions
- verification gate
- handoff gate

Use `jstack_team_plan` with `team_mode="full-team"` and
`jstack_dispatch_check` with `team_mode="full-team"` and
`coordination_packet_supplied=true` when available. If multi-agent tools are
unavailable, write `No subagents deployed:` and give the concrete reason, then
continue with the single-lead enterprise workflow while manually applying the
full-team review rubric.

When concurrency would create noise, dispatch the full team in waves:

1. Discovery: Architect, Code Investigator, Product/UX or Quant when relevant.
2. Build: Builder only after Lead approval of scope.
3. Review: Reviewer, QA, Security, DevOps, Documentation.
4. Synthesis: Lead reconciles findings, verifies, and hands off.
