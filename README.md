# ChatGPT Engineering Delivery

Engineering Delivery is a separate lifecycle role from Product Governance, Local Agent execution, Independent Product Experience Review, Human Owner acceptance, merge and release.

Current staged successor version: `0.2.2-alpha`.

## Core rule

Engineering Delivery converts one frozen Goal/Milestone Contract into one exact-SHA technical candidate and may declare only the Engineering terminal defined by the contract.

It owns source/tests/technical remediation/commit/push/PR/CI/exact candidate/Candidate Manifest/Technical Receipt. It does not change product meaning without Change Request and does not perform Owner-machine local operations.

## Local execution

Owner-designated Local Agent is the sole local executor. When deployment/runtime materialization is requested, post-deployment operational verification is mandatory. Local Agent output is observation evidence only.

## Visual-product work

Human Owner ecosystem authority: `zhouzengrui369-commits/knowme-ecosystem#39`.

For visual-product work:

```text
ENGINEERING_VISUAL_EVIDENCE_REQUIRED=YES
HUMAN_REVIEWABLE_VISUAL_EVIDENCE=COMPLETE
ENGINEERING_VISUAL_EVIDENCE_INSPECTED=YES
ENGINEERING_PERSONAL_EVIDENCE_INSPECTION_REQUIRED=YES
ENGINEERING_VISUAL_CONFORMANCE=PASS
```

Engineering Delivery must personally open/view the actual visual evidence bytes. Screenshot counts, gate PASS text, Local Agent self-declared visual PASS or hashes without viewing the corresponding evidence are insufficient.

Local Agent may capture/record/package/hash/sanitize/return visual evidence, but it does not own Engineering visual conformance, Demo return, Product Experience or Human Owner verdicts.

See:

- `core/ENGINEERING_DELIVERY_SKILL.md`
- `core/VISUAL_EVIDENCE_POLICY.md`
- `contracts/LOCAL_EXECUTION.md`

```text
LOCAL_AGENT_OBSERVATION
!= ENGINEERING_ADJUDICATION
ENGINEERING_VISUAL_CONFORMANCE_PASS
!= ENGINEERING_READY
!= PRODUCT_EXPERIENCE_PASS
!= HUMAN_OWNER_ACCEPTED
```
