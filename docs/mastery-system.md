# JStack Mastery System

## Purpose

JStack is a training and execution system for professional software delivery.
The goal is not to make agents produce more text. The goal is to build
source-backed, tested, reviewable, production-safe changes while training the
operator to think like a senior engineer.

## Stage 0: Operator Setup

Outcome: You can navigate the environment without causing damage.

Core principles:

- know the working directory
- know the repo state
- never run destructive commands casually
- understand local vs production boundaries
- keep secrets out of prompts, commits, and logs

Benchmarks:

- can explain the current project path and git branch
- can inspect status before editing
- can identify files that must not be touched
- can distinguish local test work from deploy/release work

## Stage 1: Code Reading

Outcome: You can trace existing behavior before asking for or accepting edits.

Core principles:

- read before changing
- prefer source truth over assumptions
- identify entrypoints, contracts, and tests
- understand the existing design style

Benchmarks:

- can name the relevant files and functions
- can explain current behavior from code references
- can identify likely blast radius
- can ask for the right missing evidence

## Stage 2: Scoped Fixes

Outcome: You can complete small changes without unrelated churn.

Core principles:

- smallest coherent diff
- local conventions first
- no drive-by refactors
- tests proportional to risk

Benchmarks:

- can state exactly what changed and why
- can show focused verification
- can spot unrelated modifications
- can reject broad rewrites for narrow bugs

## Stage 3: Testing and Debugging

Outcome: You can reproduce, isolate, fix, and verify a defect.

Core principles:

- reproduce before fixing
- isolate root cause
- change one variable at a time
- prove the fix with targeted checks

Benchmarks:

- can produce a minimal reproduction
- can separate symptom from cause
- can explain why the fix works
- can report residual risk honestly

## Stage 4: Backend, API, and Data Contracts

Outcome: You can protect schemas, APIs, data flows, and failure modes.

Core principles:

- contracts are promises
- migrations need rollback thinking
- invalid data must fail visibly
- integration behavior needs source-backed tests

Benchmarks:

- can identify contract boundaries
- can describe migration risk
- can verify API and data behavior
- can detect hidden coupling

## Stage 5: Frontend and Product Execution

Outcome: You can evaluate whether the user experience actually works.

Core principles:

- build the real workflow, not a decorative shell
- verify responsive behavior
- avoid overlapping UI and vague UX
- use screenshots and runtime checks

Benchmarks:

- can define acceptance criteria from user intent
- can inspect browser/runtime behavior
- can identify visual or interaction regressions
- can distinguish product value from visual polish

## Stage 6: DevOps and Release

Outcome: You can ship without confusing coding with deployment.

Core principles:

- deploy requires explicit approval
- preflight comes before release
- rollback must exist before risk
- logs and monitoring matter after deploy

Benchmarks:

- can list predeploy checks
- can produce a rollback plan
- can explain environment separation
- can define canary or monitoring checks

## Stage 7: Security and Reliability

Outcome: You can identify trust boundaries and release blockers.

Core principles:

- secrets never belong in code or chat
- auth and RBAC need explicit review
- public surfaces need threat modeling
- reliability includes failure behavior

Benchmarks:

- can identify sensitive paths and data
- can explain likely abuse cases
- can verify secrets are not exposed
- can mark security blockers clearly

## Stage 8: Architecture

Outcome: You can design changes that remain maintainable.

Core principles:

- architecture is constraint management
- abstractions must pay rent
- compatibility matters
- observability is part of design

Benchmarks:

- can explain tradeoffs
- can identify invariants
- can design a migration path
- can reject premature abstraction

## Stage 9: Staff-Level Execution

Outcome: You can convert ambiguity into a shipped, monitored, documented result.

Core principles:

- reduce uncertainty
- sequence work by risk
- keep stakeholders informed
- leave the system easier to operate

Benchmarks:

- can turn vague requests into phases
- can coordinate specialists without chaos
- can make go/no-go calls from evidence
- can hand work off cleanly

## Practice Loop

For every non-trivial JStack task:

1. identify the current mastery stage
2. state the learning objective
3. define the expert mental model
4. complete the work through the right gates
5. score the evidence
6. define the next drill

## Skill Score

| Score | Label | Meaning |
| --- | --- | --- |
| 0 | Observed only | Can follow the result but cannot explain or reproduce it |
| 1 | Guided | Can execute with step-by-step support |
| 2 | Competent | Can use a checklist and explain verification |
| 3 | Advanced | Can adapt the workflow and catch common failures |
| 4 | Expert | Can design, review, and teach the workflow |
