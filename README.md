# JStack Commands

Custom Codex slash commands, skill, MCP server, and policy templates for
enterprise-grade software work.

JStack is our project-specific wrapper around the upstream gstack workflow. The
user-facing command surface is JStack; upstream gstack skills remain available
as implementation building blocks where useful.

## Commands

- `/j-stack-dev` - single Lead Engineer workflow; no subagents by default.
- `/jstack-subagents` - Lead Engineer plus the right specialist team, normally
  2-3 specialists.
- `/jstack-full-team` - full 11-role JStack team for major, high-risk, or
  explicitly requested full-team work.

## Included

- `plugin/` - installable Codex plugin package for universal slash commands.
- `plugin/commands/` - global `/j-stack-dev`, `/jstack-subagents`, and
  `/jstack-full-team` command definitions.
- `prompts/j-stack-dev.md` - single-lead slash command.
- `prompts/jstack-subagents.md` - smart specialist-team slash command.
- `prompts/jstack-full-team.md` - full-team slash command.
- `skills/jstack-dev/SKILL.md` - full operating workflow and mastery system.
- `mcp/jstack/jstack_mcp_server.py` - local stdio MCP server.
- `mcp/jstack/templates/` - enterprise policy, release, PR, team, and quant templates.
- `examples/jstack.enterprise.json` - starter project policy.
- `scripts/install.py` - cross-platform installer for Codex.
- `scripts/install.ps1` - Windows PowerShell wrapper.

## MCP Tools

The JStack MCP exposes `jstack_*` tools:

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

Legacy `gstack_*` tool aliases are retained for compatibility, but new prompts
and docs should use `jstack_*`.

## Install

### Universal Codex Plugin

This is the preferred install path. It makes the commands available globally in
Codex threads and projects through the plugin command registry.

On this machine the plugin is registered from the personal marketplace at:

```text
C:\Users\TE05\.agents\plugins\marketplace.json
```

Install or refresh it with:

```powershell
python C:\Users\TE05\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py C:\Users\TE05\plugins\jstack
python C:\Users\TE05\.codex\skills\.system\plugin-creator\scripts\update_plugin_cachebuster.py C:\Users\TE05\plugins\jstack
& C:\Users\TE05\AppData\Roaming\npm\codex.cmd plugin add jstack@personal
```

After installing, restart Codex or open a new thread so the command registry
reloads.

### Legacy Direct Install

This path copies prompt files, the skill, and the MCP server directly into
`~/.codex`. It is kept for compatibility, but the plugin install above is the
global slash-command route.

From the repo root:

```powershell
python .\scripts\install.py
```

Or on Windows:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\install.ps1
```

Restart Codex or open a new thread after installing so custom commands and MCP
tools reload.

## Smoke Test

```powershell
python .\mcp\jstack\smoke_test.py
```

Expected:

```text
jstack MCP smoke test passed
```

## Project Policy

Copy this into a project root and customize it:

```text
examples/jstack.enterprise.json
```

The MCP will look for:

- `jstack.enterprise.json`
- `jstack.policy.json`
- `jstack.yml`
- `.jstack/jstack.enterprise.json`
- `.jstack/jstack.yml`

Legacy `gstack.*` policy files are still accepted so existing projects do not
break during migration.

## Operating Standard

Small tasks stay single-lead. Complex tasks use a controlled lead-plus-
specialists model. Specialists are read-only by default. Any editing specialist
must have a disjoint write scope. The Lead Engineer owns final synthesis,
verification, and handoff.

This is intentionally not an uncontrolled swarm executor.
