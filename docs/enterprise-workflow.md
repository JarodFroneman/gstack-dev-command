# Enterprise JStack Workflow

## Commands

1. `/j-stack-dev`: single Lead Engineer, no subagents by default.
2. `/jstack-subagents`: Lead Engineer plus the right specialist team, normally
   2-3 specialists.
3. `/jstack-full-team`: full 11-role JStack team for major or explicitly
   requested full-team work.

## Gates

1. Classify task risk.
2. Restore context and read project instructions.
3. Create an enterprise plan.
4. Build a team plan and coordination packet when risk justifies specialists.
5. Run policy and preflight checks.
6. Implement the smallest coherent change.
7. Review, test, QA, and security-check proportionally to risk.
8. Run release readiness only when release/deploy is explicitly requested.
9. Save handoff context and document residual risk.

## Production Controls

- policy-as-code
- agent coordination packet
- file ownership map
- protected-path checks
- diff hygiene
- test command discovery
- secret scan
- release approval
- rollback plan
- canary or monitoring plan
- quant/backtest evidence gates

## Mastery Path

0. Operator setup
1. Code reading
2. Scoped fixes
3. Testing and debugging
4. Backend/API/data contracts
5. Frontend and product execution
6. DevOps and release
7. Security and reliability
8. Architecture
9. Staff-level execution
