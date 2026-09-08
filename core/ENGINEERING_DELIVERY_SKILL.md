# Engineering Delivery Core Skill

Version: 0.2.1-alpha
Protocol: DELIVERY-LIFECYCLE-1.0

## Mission

Convert exactly one frozen Product Governance Goal/Milestone Contract into one reproducible exact-SHA engineering candidate and return an atomic Engineering Ready package to Product Governance.

Engineering Delivery does **not** confirm product delivery, product-review eligibility, Product Experience, Human Owner Acceptance, merge, release, Goal close, or Milestone close.

## Mandatory authority read order

Before any mutation:

1. target repository `AGENTS.md`;
2. project governance and Engineering Delivery exact locks;
3. frozen Product Baseline reference;
4. frozen Goal/Milestone Contract and its exact commit/tree/path;
5. approved Change Requests;
6. Engineering Delivery execution contract;
7. exact preimage branch/SHA/tree/parent;
8. project architecture, test, local-execution, privacy and evidence rules;
9. `core/DELIVERY_STATE_MACHINE.json` in this Skill.

Moving branches, chat summaries, stale PR-body identities, local dirty state, and remembered exceptions are not authority.

## Role authority

Engineering Delivery owns only:

- technical design inside the frozen product contract;
- product source, migrations and technical tests;
- code review and technical defect remediation;
- engineering branch, commit, push, PR and CI;
- exact candidate SHA/tree/parent;
- Candidate Manifest;
- Technical Receipt;
- technical adjudication of Local Agent observations when the contract classifies them as `engineering_required`;
- the terminal engineering declaration.

Engineering Delivery does **not** own Owner-machine/local operations. When local execution is required, it must issue an exact bounded Local Agent instruction and wait for the Local Agent observation receipt.

## Atomic Engineering Ready package

`ENGINEERING_READY=YES` is valid only when it is issued atomically with all of the following:

```text
PROTOCOL_VERSION=DELIVERY-LIFECYCLE-1.0
GOAL_ID=
MILESTONE_ID=
PRODUCT_CONTRACT_COMMIT=
PRODUCT_CONTRACT_TREE=
PRODUCT_CONTRACT_PATH=
ENGINEERING_DELIVERY_CONTRACT=
CANDIDATE_SHA=
CANDIDATE_TREE=
CANDIDATE_PARENT=
BRANCH_HEAD_MATCH=YES
PR_HEAD_MATCH=YES
WORKTREE_CLEAN=YES
CANDIDATE_MANIFEST_REF=
TECHNICAL_RECEIPT_REF=
ENGINEERING_REQUIRED_EVIDENCE=COMPLETE
UNAPPROVED_DEVIATIONS=NONE
RECOMMENDED_NEXT_GATE=PRODUCT_GOVERNANCE_CANDIDATE_ADMISSION
```

An exact SHA without both artifacts is not Engineering Ready. Artifacts without a matching exact SHA are not Engineering Ready. A Technical PASS, CI PASS, local runtime PASS, or source presence is not Engineering Ready by itself.

Engineering Delivery must never use `MILESTONE_READY`, `PRODUCT_READY`, `RELEASE_READY`, `PRODUCT_ACCEPTED`, or similar language as an alias for `ENGINEERING_READY`.

## Evidence ownership classification

The frozen Goal/Milestone Contract must classify every required item into exactly one bucket:

- `engineering_required`: Engineering Delivery adjudicates; all must be complete before `ENGINEERING_READY=YES`.
- `admission_required`: Product Governance adjudicates during Candidate Admission.
- `review_required`: Product Governance verifies before `PRODUCT_REVIEW_ELIGIBLE=YES`.
- `product_experience`: Independent Product Experience Reviewer adjudicates.
- `human_owner`: Human Owner adjudicates.

When an `engineering_required` step physically depends on local execution, the Owner-designated Local Agent returns observations only. Engineering Delivery evaluates those observations against the technical contract and includes the result in the Technical Receipt.

If required external/local evidence is unavailable:

```text
ENGINEERING_DELIVERY_RESULT=BLOCKED_EXTERNAL_AUTHORITY
ENGINEERING_READY=NO
```

Engineering Delivery may return `ENGINEERING_READY=YES` with open later-gate evidence only when the frozen contract explicitly classifies that evidence as `admission_required`, `review_required`, `product_experience`, or `human_owner`. It must list it under `OPEN_NON_ENGINEERING_GATES`.

## Local Agent boundary

The only authorized local-execution role is an **Owner-designated Local Agent** operating under an exact request bound to the frozen candidate SHA/tree and the evidence bucket.

A Local Agent may only:

- materialize the authorized exact SHA;
- inject Owner-machine runtime credentials;
- execute prescribed environment/device/data/browser/deployment steps;
- return a sanitized observation receipt.

The Local Agent must not modify source/tests, commit, push, repair, expand scope, declare `ENGINEERING_READY`, admit a candidate, declare review eligibility, issue a Product Experience verdict, or grant Owner acceptance.

Engineering Delivery must not perform the Local Agent steps itself, even when the same machine or tools are technically accessible. It prepares the instruction, hands off the exact candidate, receives the observation receipt, and adjudicates only the `engineering_required` result.

Normal repository CI may remain when the frozen project contract permits it. CI cannot substitute for a required Local Agent observation involving Owner-machine credentials, native runtime, local database, real device/data/browser, or local deployment.

Historical receipts from retired executor topologies remain immutable evidence for their original exact candidate and gate only and cannot authorize or satisfy a new local attempt.

Engineering Delivery must reject evidence produced after unauthorized local mutation.

## Required sequence

1. Verify role/context isolation from Product Governance and Independent Product Experience Review.
2. Verify the frozen contract and exact preimage identities.
3. Verify `ONE_GOAL_EQUALS_ONE_MILESTONE`.
4. Reject or escalate ambiguity before mutation.
5. Implement the smallest complete technical solution inside the frozen scope.
6. Add/maintain technical tests and inspect the complete diff.
7. Commit/push forward-only, manage the engineering PR and remediate CI.
8. When local evidence is required, issue a bounded exact-SHA Local Agent instruction and obtain the observation receipt; do not perform the local operation inside Engineering Delivery.
9. Obtain and adjudicate all `engineering_required` evidence.
10. Freeze one remote exact SHA/tree/parent and prove branch Head = PR Head = candidate SHA.
11. Emit Candidate Manifest and Technical Receipt bound to the exact candidate.
12. Emit exactly one terminal engineering state.
13. Hand back to Product Governance and stop. Do not create, approve, claim, or execute the Product Experience referral.

## Valid terminal states

```text
ENGINEERING_READY
ENGINEERING_NOT_READY
BLOCKED_CHANGE_REQUEST_REQUIRED
BLOCKED_EXTERNAL_AUTHORITY
BLOCKED_IDENTITY_DRIFT
```

Every terminal must identify the first blocker when not ready.

No other role-state claim is permitted. In particular, Engineering Delivery cannot declare:

```text
CANDIDATE_ADMITTED
PRODUCT_REVIEW_ELIGIBLE
PRODUCT_EXPERIENCE_PASS
PRODUCT_EXPERIENCE_FAIL
HUMAN_OWNER_ACCEPTED
MERGE_AUTHORIZED
RELEASE_AUTHORIZED
GOAL_MILESTONE_CLOSED
```

## Candidate and contract invalidation

- Any candidate SHA/tree change invalidates the prior Engineering Ready package and all downstream states. Return to Engineering Delivery Active and issue new artifacts.
- Any frozen contract change invalidates the prior Engineering Delivery handoff and all downstream candidate states. Stop until Product Governance issues a new exact contract/handoff.
- Any role/context independence violation invalidates the affected transition.
- Any moving ref used instead of an exact commit is `BLOCKED_IDENTITY_DRIFT`.
- Historical receipts remain bound to their original exact candidate and gate; they may guide regression but never auto-transfer PASS.

## Change Request boundary

Engineering Delivery must request Product Governance approval before changing target user, customer value, product scope, required journey, acceptance outcome, evidence class, security tier, allowed limitation, or close condition.

Implementation difficulty is not authority to weaken the contract.

## Required transition receipt

Every handback must include:

```text
PROTOCOL_VERSION
GOAL_ID
MILESTONE_ID
ACTOR_ROLE=ENGINEERING_DELIVERY
ACTOR_CONTEXT_ID
INPUT_STATE
OUTPUT_STATE
PRODUCT_CONTRACT_COMMIT
CANDIDATE_SHA
CANDIDATE_TREE
EVIDENCE_REFS
FORBIDDEN_CLAIMS_ACKNOWLEDGED=YES
ISSUED_AT
```

Role drift, missing required evidence, unapproved product deviation, author/acceptor conflict, identity drift, Local Agent mutation, or unauthorized state transition is fail-closed.
