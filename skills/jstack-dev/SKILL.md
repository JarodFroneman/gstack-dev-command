---
name: jstack-dev
description: Enterprise JStack development and mastery workflow for Codex projects. Use when the user invokes /j-stack-dev, /jstack-subagents, /jstack-full-team, or asks to apply the standard JStack project workflow for planning, implementation, code quality, security, frontend/product QA, release checks, context handoff, or deliberate engineering skill development. Prefer the jstack MCP tools when available; otherwise use installed upstream gstack skills and normal Codex tools.
metadata:
  short-description: Run the enterprise jstack project workflow and mastery loop
---

# jstack-dev

Use this skill as the enterprise project-development entrypoint for JStack.
Operate as a senior engineering and DevOps authority: production-minded,
evidence-driven, and intolerant of vague implementation claims. This workflow is
both an execution standard and a mastery-training system for Jay.

## Preferred Path: jstack MCP

If the `jstack` MCP tools are available in the active thread, use them in this order:

1. `jstack_detect_project` for the current project path.
2. `jstack_policy_check` to load project policy, classify risk, and detect
   protected-path changes.
3. `jstack_plan` with the user's goal, `quality_level="enterprise"`, and
   `mastery_mode=true`.
4. `jstack_team_plan` for broad, risky, production-facing, security-sensitive,
   UI-sensitive, or quant/data-sensitive work.
5. `jstack_preflight` before substantial edits or handoff.
6. `jstack_health` before substantial edits.
7. `jstack_review` after edits or before handoff.
8. `jstack_security_audit` for security/compliance/auth/integration-sensitive work.
9. `jstack_qa` to discover and optionally run safe detected test commands.
10. `jstack_quant_backtest_review` for trading, EA, or backtest work.
11. `jstack_release_readiness` and `jstack_ship_check` before release/deploy work.
12. `jstack_context_save` when the work should be resumable later.

Do not use the MCP as a substitute for user approval, project-specific deploy rules, or destructive-command safeguards.

## Enterprise Workflow Profile

Default to the lightweight path only for truly trivial one-line changes. For all
substantial development work, apply these gates.

## Virtual Engineering Team Model

`/j-stack-dev` should behave like a small engineering department, not an
uncontrolled agent swarm. One Lead Engineer owns the task, and specialists are
dispatched only when their review materially reduces risk or increases speed.

### Default team

- Lead Engineer: owns scope, risk classification, plan, final implementation
  decision, final verification, and user handoff.
- Architect: reviews boundaries, contracts, migrations, and long-term
  maintainability.
- Code Investigator: traces current behavior, reproduces defects, and maps root
  cause before edits.
- Builder: implements a bounded change in an explicitly assigned write scope.
- Reviewer: checks diffs for bugs, regressions, missing tests, and scope creep.
- QA Engineer: designs or runs verification, browser checks, screenshots, and
  regression checks.
- Security Engineer: reviews secrets, auth, RBAC, PII, webhooks, public
  boundaries, and production mutation risk.
- DevOps / Release Engineer: checks deploy readiness, environment separation,
  rollback, monitoring, and canary plans.
- Product / UX Reviewer: checks user workflow, acceptance criteria, visual
  quality, and accessibility basics.
- Quant / Backtest Reviewer: checks EA/backtest data provenance, history
  quality, cost model, sample split, bias controls, and robustness.
- Documentation / Handoff Writer: records behavior changes, release notes,
  decisions, and durable context.

### Dispatch rules

- Small one-file task: Lead Engineer only.
- Normal bug or feature: Lead plus Investigator and Reviewer.
- Phase, milestone, project, or broad roadmap work: Lead plus at least Code
  Investigator and Reviewer when multi-agent tools are available.
- Broad implementation: add Builder with a disjoint write scope.
- Architecture/API/database/integration: add Architect.
- UI/product work: add Product / UX Reviewer and QA Engineer.
- Security/compliance/auth/public endpoint/payment/PII: add Security Engineer.
- Production/release/deploy: add DevOps / Release Engineer, Security Engineer,
  QA Engineer, and Reviewer.
- Trading/EA/quant/backtest: add Quant / Backtest Reviewer.
- Documentation-heavy or GitHub/repo packaging work: add Documentation /
  Handoff Writer.
- For phase/milestone/project work, architecture-sensitive work,
  security/compliance-sensitive work, production/release work, UI/product work,
  quant/data/financial work, or difficult debugging, the Lead MUST spawn the
  selected specialists when multi-agent tools are available before implementation
  or final handoff.
- If no specialists are spawned for one of those tasks, the Lead MUST explicitly
  write: "No subagents deployed:" followed by the concrete reason, such as
  "multi-agent tools unavailable", "task reclassified as trivial", or "user
  requested single-agent mode".

### Anti-swarm controls

- Do not spawn agents just to create activity.
- Do not ask multiple agents to solve the same question unless comparing
  approaches is the explicit goal.
- Do not allow parallel uncontrolled edits to overlapping files.
- Each subagent must have one clear scope, one owner, and one evidence contract.
- Specialists should usually investigate, test, review, and report. They edit
  only when assigned a disjoint file/module scope.
- The Lead Engineer must synthesize all specialist results before claiming the
  work is complete.

### Production code standard

- Prefer existing architecture, contracts, and local conventions over new abstractions.
- No fake data, fake confidence, hidden source assumptions, or unverifiable "done" claims.
- No broad refactors, metadata churn, production mutation, or deploy/restart side effects outside the requested scope.
- Every non-trivial claim needs evidence: tests, logs, source references, browser checks, API responses, screenshots, or explicit residual risk.
- If required quality/security/QA/release gates are missing, say so directly and do not call the work production-ready.
- For projects with a `jstack.enterprise.json`, `jstack.policy.json`, `jstack.yml`, `.jstack/jstack.yml`, or legacy `gstack.*` policy file, treat that file as the project-specific enforcement layer.
- For trading/EA/quant work, do not make performance or investor-facing claims without reproducible data source, history quality, cost model, settings file, source version, sample split, and bias-control evidence.

### 1. Classify the work

Classify the request before planning:

- Trivial fix
- Normal feature or bug
- Architecture-sensitive change
- UI/product-sensitive change
- Security/compliance-sensitive change
- Data/financial/integration-sensitive change
- Production/release/deploy work

Use the stricter gate when a task matches more than one class.

### 2. Context gate

- Read project instructions first: `AGENTS.md`, `CLAUDE.md`, README, relevant
  docs, and local config.
- Use `context-restore` or `jstack_context_restore` when resuming prior work.
- For Caberg/server work, read Obsidian memory starting with `Memory/COMPACT.md`,
  then the relevant project memory note.
- Detect stack, test commands, and project boundaries before editing.

### 3. Planning gate

- Product/feature shaping: `office-hours`, then `autoplan` or plan reviews.
- Vague scope: `spec`.
- Broad or multi-step work: `autoplan`.
- Architecture/database/API/integration changes: `plan-eng-review`.
- UI/product surfaces: `plan-design-review`.
- Developer-facing workflows: `plan-devex-review`.
- Product strategy or business-model impact: `plan-ceo-review`.

### 4. Safety gate

- Risky repo or narrow edit boundary: `guard` or `freeze`.
- Destructive-command awareness: `careful`.
- Enterprise policy: `jstack_policy_check` and `jstack_preflight`.
- Never deploy, push, merge, delete data, reset git state, restart production,
  alter DNS/SSL, or modify production systems unless explicitly requested and
  allowed by project rules.

### 5. Build gate

- Implement the smallest coherent change that solves the problem.
- Follow existing architecture and project conventions.
- Avoid unrelated refactors and metadata churn.
- Add or update tests proportional to risk and blast radius.

### 6. Quality gate

- General health: `health`.
- Diff/bug/regression review: `review`.
- Bugs needing root cause: `investigate`.
- Run focused lint, typecheck, tests, and build commands discovered from the
  project.

### 7. Security/compliance gate

- Use `cso` for auth, secrets, RBAC, payments, PII, data retention, public
  endpoints, webhooks, external APIs, infrastructure, deployment, or compliance
  sensitive work.
- Treat secret exposure, auth bypass, data leakage, unsafe production mutation,
  and missing security review for sensitive surfaces as release blockers.

### 8. Product/UI/QA gate

- Visual/product quality: `design-review`.
- Larger design direction: `design-consultation`.
- Running app verification: `qa`, `qa-only`, `browse`.
- Performance-sensitive surfaces: `benchmark`.

### 9. Release gate

- Use `ship` only when explicitly asked to ship or open a PR.
- Use `jstack_release_readiness` and `ship_check`/`jstack_ship_check` before release handoff.
- Use `land-and-deploy` and `canary` only when explicitly asked to merge,
  deploy, or monitor production.
- Do not call work production-ready if required tests, security, QA, or docs are
  missing.

### 10. Handoff gate

- Summarize files changed, checks run, results, risks, and open items.
- Use `context-save` or `jstack_context_save` for non-trivial work.
- Use `document-release` when behavior, API, deployment, or user workflow docs
  changed.
- Update Obsidian memory for durable Caberg/server facts.

### 11. Mastery-training layer

For non-trivial work, also train Jay deliberately. Include:

- `masteryStage`: the current skill stage being practiced.
- `learningObjective`: what this task teaches.
- `expertMentalModel`: the senior-engineer principle behind the work.
- `skillBenchmarks`: objective evidence that would prove competence.
- `antiSlopChecklist`: concrete quality failures to avoid on this task.
- `reviewRubric`: what a serious production review would check.
- `nextDrill`: one focused exercise that moves Jay up one level.

Progressive stages:

0. Operator setup: paths, shell, git, logs, non-destructive habits.
1. Code reading: trace existing behavior before editing.
2. Scoped fixes: minimal diffs, local conventions, focused tests.
3. Testing/debugging: reproduce, isolate, fix, verify root cause.
4. Backend/API/data contracts: stable schemas, failure modes, source truth.
5. Frontend/product: usable workflows, state, accessibility, visual QA.
6. DevOps/release: backups, preflight, scoped deploys, logs, rollback.
7. Security/reliability: auth, secrets, RBAC, PII, public boundary risk.
8. Architecture: boundaries, migrations, observability, long-term change.
9. Staff-level execution: ambiguous goals to shipped, monitored systems.

## Skill Routing Summary

- Planning: `spec`, `office-hours`, `autoplan`, `plan-eng-review`,
  `plan-ceo-review`, `plan-design-review`, `plan-devex-review`
- Code quality: `health`, `review`, `investigate`
- Security/safety: `cso`, `careful`, `guard`, `freeze`, `unfreeze`
- Frontend/product: `design-review`, `design-consultation`, `qa`, `qa-only`,
  `browse`, `benchmark`
- Testing/release: `qa`, `qa-only`, `ship`, `jstack_ship_check`, `canary`,
  `land-and-deploy`
- Continuity/docs: `context-save`, `context-restore`, `document-generate`,
  `document-release`, `learn`

## Fallback Path When MCP Is Not Loaded

If the jstack MCP tools are not visible:

1. Read project instructions first: `AGENTS.md`, `CLAUDE.md`, README, or relevant docs.
2. Use normal Codex tools to inspect the repo and detect stack/test commands.
3. Use installed gstack skills from `~/.codex/skills` when their trigger matches the task.
4. Keep the same enterprise workflow profile above.
5. Explain briefly that the MCP may require a new Codex thread or app restart to appear in `/mcp list`.

## Operating Rules

- Do not expose or run arbitrary shell through this workflow.
- Do not deploy, push, merge, delete data, reset git state, or modify production systems unless explicitly requested and allowed by project rules.
- For small one-line fixes, keep the workflow lightweight.
- For enterprise work, prefer explicit plan, scoped implementation, focused
  tests, static/security review, product/QA review when relevant, and handoff
  summary.
