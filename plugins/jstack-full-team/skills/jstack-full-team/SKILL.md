---
name: jstack-full-team
description: Full 11-role JStack team workflow. Use when the user invokes /jstack-full-team or explicitly asks to deploy the full JStack team.
metadata:
  short-description: Deploy the full JStack team
---

# JStack Full Team

Treat this command as explicit user approval to deploy the full JStack team when multi-agent tools are available.

Full team means complete professional coverage, not uncontrolled concurrency.
The Lead Engineer may dispatch the full team in waves when that is safer or
clearer.

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
6. Before dispatch, require a coordination packet.

Coordination packet:

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

Full-team wave pattern:

1. Discovery: Architect, Code Investigator, Product/UX or Quant when relevant.
2. Build: Builder only after Lead approval of scope.
3. Review: Reviewer, QA, Security, DevOps, Documentation.
4. Synthesis: Lead reconciles evidence, resolves conflicts, verifies, and hands off.

If multi-agent tools are unavailable, state `No subagents deployed:` with the concrete reason, then continue with the single-lead workflow while manually applying the full-team review rubric.
