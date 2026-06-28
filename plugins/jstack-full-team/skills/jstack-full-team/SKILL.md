---
name: jstack-full-team
description: Full 11-role JStack team workflow. Use when the user invokes /jstack-full-team or explicitly asks to deploy the full JStack team.
metadata:
  short-description: Deploy the full JStack team
---

# JStack Full Team

Treat this command as explicit user approval to deploy the full JStack team when multi-agent tools are available.

Full roster:

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

Operating rules:

1. The Lead Engineer owns final scope, synthesis, implementation decisions, verification, and handoff.
2. Specialists are read-only by default.
3. Builder may edit only inside an explicitly assigned disjoint write scope.
4. Documentation / Handoff Writer may edit docs only when assigned.
5. If concurrency limits prevent all specialists from running at once, dispatch them in waves.

If multi-agent tools are unavailable, state `No subagents deployed:` with the concrete reason, then continue with the single-lead workflow while manually applying the full-team review rubric.
