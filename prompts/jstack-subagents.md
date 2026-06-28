---
description: Run JStack with the right specialist subagent team
argument-hint: [GOAL]
---

Apply the custom JStack enterprise development workflow to this task.

Goal:
$ARGUMENTS

Mode: `smart-subagents`.

The user invoked `/jstack-subagents`, which is explicit approval to deploy
subagents for this task when multi-agent tools are available.

Use the Lead Engineer plus the right specialist team, normally 2-3 specialists:

- For normal feature/bug work: Code Investigator + Reviewer.
- For phase/milestone/project work: Code Investigator + Reviewer, plus QA when
  verification risk is meaningful.
- For architecture/API/database/integration work: Architect + Code Investigator
  + Reviewer.
- For UI/product work: Product / UX Reviewer + QA Engineer + Reviewer.
- For security/compliance work: Security Engineer + Reviewer + QA Engineer.
- For production/release/deploy work: DevOps / Release Engineer + Security
  Engineer + QA Engineer.
- For trading/EA/quant/backtest work: Quant / Backtest Reviewer + Reviewer +
  QA Engineer.

Before spawning several specialists or assigning any file edits, create a
coordination packet:

- goal
- risk class
- roles used and why
- roles skipped and why
- read/write permissions
- file ownership map
- evidence contract
- stop conditions
- verification gate

Use `jstack_team_plan` with `team_mode="smart-subagents"` and
`jstack_dispatch_check` with `team_mode="smart-subagents"` and
`coordination_packet_supplied=true` when available. Specialists are read-only
by default. Only a Builder may edit, and only inside an explicitly assigned
disjoint write scope.

If multi-agent tools are unavailable, write `No subagents deployed:` and give
the concrete reason, then continue with the single-lead enterprise workflow.
