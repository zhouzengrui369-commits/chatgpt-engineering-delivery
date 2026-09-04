# Changelog

## 0.2.0-alpha — 2026-09-04

- Make `ENGINEERING_READY` an atomic exact-candidate package.
- Separate Engineering Ready, Candidate Admission, Product Review eligibility, Product Experience, Human Owner acceptance, and closure into role-owned states.
- Add machine-readable `DELIVERY-LIFECYCLE-1.0` state machine and fail-closed invalidation rules.
- Classify every evidence requirement as engineering, admission, review, product-experience, or Human Owner owned.
- Define Local Executor as observation-only and forbid it from issuing technical or product verdicts.
- Add stronger Goal Delivery, Candidate Manifest, Technical Receipt, Local Execution, and Engineering Terminal contracts.
- Add automated lifecycle validation.

## 0.1.0-alpha — 2026-09-03

- Bootstrap standalone Engineering Delivery Skill.
- Enforce one Goal equals one Milestone.
- Separate Engineering Delivery from Product Governance and independent product review.
