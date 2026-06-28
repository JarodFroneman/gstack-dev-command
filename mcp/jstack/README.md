# JStack MCP

Local stdio MCP server for using the JStack workflow across Codex projects.

This is intentionally a narrow orchestration layer, not a generic shell runner.
It exposes safe, project-oriented tools that help an agent apply JStack patterns
consistently:

- `jstack_detect_project`
- `jstack_list_skills`
- `jstack_read_skill`
- `jstack_plan`
- `jstack_team_plan`
- `jstack_dispatch_check`
- `jstack_policy_check`
- `jstack_preflight`
- `jstack_health`
- `jstack_review`
- `jstack_security_audit`
- `jstack_qa`
- `jstack_context_save`
- `jstack_context_restore`
- `jstack_ship_check`
- `jstack_release_readiness`
- `jstack_quant_backtest_review`

## Design Rules

- No arbitrary shell command tool.
- No network calls.
- No destructive filesystem operations.
- Test/build execution is optional and restricted to commands discovered from
  project files such as `package.json`, `pyproject.toml`, `Cargo.toml`, or
  `go.mod`.
- Context save writes only to `~/.jstack/mcp-context`.
- Upstream gstack skills are read from `~/.gstack/repos/gstack`.

## Enterprise Enforcement

The server supports policy-as-code through a project policy file. Recommended
file names:

- `jstack.enterprise.json`
- `jstack.policy.json`
- `jstack.yml`
- `.jstack/jstack.enterprise.json`
- `.jstack/jstack.yml`

Legacy `gstack.*` policy files are also accepted for migration compatibility.

Templates live in `templates/`:

- `agent_coordination_protocol.md`
- `jstack.enterprise.json`
- `jstack.enterprise.yml`
- `pull_request_template.md`
- `release_checklist.md`
- `quant_backtest_review.md`

Use `jstack_policy_check` to load project policy and detect protected file
changes. Use `jstack_preflight` before substantial edits or handoff. Use
`jstack_release_readiness` before any production release. Use
`jstack_quant_backtest_review` before making trading, EA, or backtest
performance claims.

## Virtual Engineering Team

`jstack_team_plan` turns `/j-stack-dev` into a controlled virtual engineering
team. It always keeps a Lead Engineer accountable and conditionally adds
specialists:

- Architect
- Code Investigator
- Builder
- Reviewer
- QA Engineer
- Security Engineer
- DevOps / Release Engineer
- Product / UX Reviewer
- Quant / Backtest Reviewer
- Documentation / Handoff Writer

Use `jstack_dispatch_check` before spawning several specialists or assigning
file edits. The default maximum is three specialists. More specialists require a
lead justification. Subagents are read-only by default, and only one agent may
own a given file/module write scope.

## Local Smoke Test

```bash
python3 /Users/jarodfroneman/.codex/mcp/jstack/smoke_test.py
```

## Install Into Codex

```bash
python3 /Users/jarodfroneman/.codex/mcp/jstack/install.py
```

The installer:

- copies this folder to `~/.codex/mcp/jstack`
- backs up `~/.codex/config.toml`
- adds `[mcp_servers.jstack]`

Restart Codex or open a new thread after installation.

## Operational Intent

Use this MCP as an enterprise project quality gate:

1. Classify the work by risk:
   - Trivial fix
   - Normal feature or bug
   - Architecture-sensitive change
   - UI/product-sensitive change
   - Security/compliance-sensitive change
   - Data/financial/integration-sensitive change
   - Production/release/deploy work
2. Apply the matching gate sequence:
   - Context: project instructions, restored context, project memory, project detection
   - Planning: `spec`, `office-hours`, `autoplan`, `plan-eng-review`,
     `plan-ceo-review`, `plan-design-review`, `plan-devex-review`
   - Safety: `guard`, `freeze`, `careful`
   - Build: scoped implementation using existing architecture
   - Quality: `health`, `review`, `investigate`, focused tests
   - Security/compliance: `cso`, secret scan, auth/RBAC/data/public-boundary review
   - Product/UI/QA: `design-review`, `design-consultation`, `qa`, `qa-only`,
     `browse`, `benchmark`
   - Release: `ship`, `land-and-deploy`, `canary` only when explicitly requested
   - Handoff: `context-save`, `document-release`, `learn`
3. Return required gates and release blockers from `jstack_plan`.
4. Build a lead-plus-specialists team plan when task risk justifies it.
5. Run policy and preflight checks before substantial implementation.
6. Run safe health/review/security/QA checks.
7. Run release readiness checks only when release/deploy is explicitly requested.
8. Save context for handoff or later continuation.
9. Keep project-specific production/deployment commands outside the MCP unless
   they are explicitly requested, discovered, selected, and allowed by project
   rules.
