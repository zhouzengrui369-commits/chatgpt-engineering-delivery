# ChatGPT Engineering Delivery

A repository-native Skill for converting exactly one frozen Product Governance Goal/Milestone Contract into one reproducible exact-SHA engineering candidate.

## Canonical boundary

Engineering Delivery owns technical design, product source/tests, code review, commits, PR, CI remediation, exact candidate identity, Candidate Manifest, Technical Receipt, and only the `ENGINEERING_READY` decision.

It does not own Candidate Admission, Product Review eligibility, Product Experience, Human Owner Acceptance, merge, release, Goal close, or Milestone close.

## Mandatory lifecycle

```text
Product Governance freezes one Goal/Milestone Contract
→ separate Engineering Delivery context
→ exact SHA + Candidate Manifest + Technical Receipt
→ ENGINEERING_READY
→ stop and hand back
→ Product Governance Candidate Admission
→ Product Governance PRODUCT_REVIEW_ELIGIBLE
→ Independent Product Experience Review
```

`ENGINEERING_READY` is valid only as an atomic exact-candidate package. CI PASS, test PASS, runtime PASS, or source presence alone is insufficient.

## Read order

1. `core/ENGINEERING_DELIVERY_SKILL.md`
2. `core/DELIVERY_STATE_MACHINE.json`
3. `contracts/GOAL_DELIVERY.md`
4. target repository `AGENTS.md`
5. target frozen Goal/Milestone Contract and exact locks

Core invariant: **one Goal = one Milestone = one Engineering Delivery contract**.
