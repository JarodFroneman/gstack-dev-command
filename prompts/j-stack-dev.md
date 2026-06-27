---
description: Run JStack enterprise workflow in single-lead mode
argument-hint: [GOAL]
---

Apply the custom JStack enterprise development workflow to this task.

Goal:
$ARGUMENTS

Mode: `single-lead`.

This command is intentionally the non-subagent version. Do not spawn subagents
unless the user separately and explicitly asks for subagents in the same prompt.

Use one Lead Engineer to run the enterprise gates:

1. Classify risk.
2. Read project instructions and restore context.
3. Use `jstack_detect_project`, `jstack_policy_check`, `jstack_plan`, and
   `jstack_preflight` when available.
4. Implement the smallest coherent change.
5. Run focused review, security, QA, release, or quant checks required by the
   risk class.
6. Report files changed, checks run, residual risk, and next steps.

If the `jstack_*` MCP tools are unavailable, use the installed `jstack-dev`
skill and normal Codex tools, then state that a Codex restart/new thread may be
needed for MCP refresh.
