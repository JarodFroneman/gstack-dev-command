---
name: j-stack-dev
description: Single Lead Engineer JStack workflow. Use when the user invokes /j-stack-dev or asks for the standard JStack development workflow without subagents.
metadata:
  short-description: Run JStack as a single Lead Engineer
---

# JStack Dev

Use the JStack Think -> Plan -> Build -> Review -> Test -> Ship structure.

Default behavior:

1. Operate as the Lead Engineer.
2. Do not deploy subagents by default.
3. Use installed `jstack_*` MCP tools when available for project detection, planning, health checks, review checks, security checks, QA command discovery, release readiness, and context save or restore.
4. If `jstack_*` tools are unavailable, fall back to the installed upstream `gstack-*` skills and normal Codex workflow.
5. Respect project `AGENTS.md`, safety rules, branch/deploy rules, and explicit user approvals.

This command is for substantial development work. Tiny one-line fixes may use normal Codex workflow.
