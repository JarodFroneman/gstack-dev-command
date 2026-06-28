# /j-stack-dev

Run JStack in single-lead mode for the current task.

## Arguments

- `goal`: the task or project objective to execute.

## Workflow

1. Treat this command as the non-subagent version of JStack.
2. Do not deploy subagents unless the user separately and explicitly asks for subagents in the same prompt.
3. Use one Lead Engineer to classify risk, read project instructions, plan, implement, verify, and hand off.
4. Prefer `jstack_detect_project`, `jstack_policy_check`, `jstack_plan`, and `jstack_preflight` when available.
5. Run focused review, security, QA, release, or quant checks required by the risk class.
6. Report files changed, checks run, residual risk, and next steps.

## Fallback

If `jstack_*` MCP tools are unavailable, use the `jstack-dev` skill and normal Codex tools, then state that a Codex restart or new thread may be needed for MCP refresh.
