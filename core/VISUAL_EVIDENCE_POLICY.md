# Engineering Delivery Visual Evidence Policy

Version: 0.1.0-alpha
Protocol: DELIVERY-LIFECYCLE-1.0
Authority: `zhouzengrui369-commits/knowme-ecosystem#39`

## Applicability

`VISUAL_WORK_CLASS=YES` whenever the frozen Goal/Milestone Contract or approved exact addendum materially includes one or more of:

```text
VISUAL_BASELINE
DEMO_RETURN
UI
LAYOUT
PRODUCT_SHELL
VISUAL_INHERITANCE
RESPONSIVE_LAYOUT
2D_3D_VISUAL_BEHAVIOR
INTERACTION_CONTINUITY
ANIMATION_OR_MOTION
```

Engineering Delivery must follow the exact project classification. If obvious visual work is unclassified, stop with the appropriate contract/change-request blocker rather than silently treating it as non-visual.

## Visual Engineering Ready gate

For `VISUAL_WORK_CLASS=YES`, the normal atomic Engineering Ready package is insufficient unless all of these are also established:

```text
ENGINEERING_VISUAL_EVIDENCE_REQUIRED=YES
HUMAN_REVIEWABLE_VISUAL_EVIDENCE=COMPLETE
ENGINEERING_VISUAL_EVIDENCE_INSPECTED=YES
ENGINEERING_PERSONAL_EVIDENCE_INSPECTION_REQUIRED=YES
ENGINEERING_VISUAL_CONFORMANCE=PASS
TEXT_RECEIPT_ONLY_SUFFICIENT=NO
LOCAL_AGENT_SELF_DECLARED_VISUAL_PASS_SUFFICIENT=NO
```

Missing any required item forbids `ENGINEERING_READY=YES`.

## Personal inspection

Engineering Delivery must itself open/view the actual human-reviewable visual evidence bytes. Reading textual summaries, hashes without rendering the corresponding evidence, screenshot counts or Local Agent/gate PASS fields does not satisfy this requirement.

Examples of insufficient evidence by themselves:

```text
SCREENSHOT_COUNT=88
DEMO_PAIRED_EVIDENCE=PASS
VISUAL_GATE=PASS
LOCAL_AGENT_VISUAL_PASS=PASS
```

Engineering Delivery must inspect the paired screenshots, page captures, interaction captures/contact sheets and video/continuous evidence applicable to the frozen contract before setting `ENGINEERING_VISUAL_CONFORMANCE=PASS|FAIL`.

## Minimum evidence package

The package must include, as applicable:

1. Demo/reference ↔ candidate paired screenshots;
2. complete screenshots of core product pages/surfaces;
3. key interaction before/after captures;
4. contact sheet and/or video/continuous capture for dynamic interaction;
5. protected responsive viewports;
6. visual difference index;
7. exact candidate identity;
8. SHA256 evidence-integrity manifest;
9. source/test/runtime evidence mapping.

Every evidence item/index entry must identify enough metadata to answer:

```text
WHAT_AM_I_LOOKING_AT
WHICH_CANDIDATE
WHICH_VIEWPORT
WHICH_PRODUCT_STATE
WHICH_REQUIREMENT
WHICH_DEMO_REFERENCE
WHAT_DIFFERENCE_IS_VISIBLE
WHAT_AUTHORITY_MAY_ALLOW_THE_DIFFERENCE
```

A Local Agent or evidence generator prepares the difference index with:

```text
ENGINEERING_ADJUDICATION=PENDING
```

Engineering Delivery records `PASS|FAIL` only after personal inspection.

## Required Technical Receipt fields

For visual work the fresh Technical Receipt must include:

```text
ENGINEERING_VISUAL_EVIDENCE_REQUIRED=YES
HUMAN_REVIEWABLE_VISUAL_EVIDENCE=COMPLETE
ENGINEERING_VISUAL_EVIDENCE_INSPECTED=YES
ENGINEERING_PERSONAL_EVIDENCE_INSPECTION_REQUIRED=YES
ENGINEERING_VISUAL_CONFORMANCE=PASS|FAIL
ENGINEERING_VISUAL_EVIDENCE_REFS=<exact durable refs>
ENGINEERING_VISUAL_EVIDENCE_SHA256_MANIFEST_REF=<exact ref>
ENGINEERING_VISUAL_INSPECTION_NOTES=<bounded findings>
```

Engineering visual conformance is limited to the engineering-owned requirements in the frozen contract/addendum. It is not Demo-return acceptance, Product Experience PASS or Human Owner acceptance.

## Local Agent boundary

Local Agent may only capture, record, package, hash, sanitize and return visual evidence under the exact request. It must not claim Demo return, visual parity, Engineering visual conformance, Product Experience or Human Owner acceptance.

This policy gives Local Agent no source/test/commit/push/PR/governance mutation or self-repair authority.

## Durable evidence / candidate identity

Human-reviewable evidence may be attached to an authoritative Issue/PR or stored in independent evidence storage with exact refs and SHA256 integrity records.

Do not commit screenshots/video into the product candidate merely to make evidence durable if doing so changes the candidate SHA being evidenced.

```text
COMMIT_VISUAL_EVIDENCE_INTO_PRODUCT_CANDIDATE_IF_NEW_SHA=FORBIDDEN
PRODUCT_CANDIDATE_SHA_MUST_NOT_CHANGE_FOR_EVIDENCE_PACKAGING=YES
```

## Exact-SHA technical evidence reuse

A fresh evidence-only Engineering re-entry may reuse prior exact-SHA technical evidence only by fresh Engineering adjudication when:

```text
CANDIDATE_SHA_UNCHANGED
AND EVIDENCE_IDENTITY_MATCHES
AND NO_RUNTIME_OR_SOURCE_DRIFT
```

Historical receipts are evidence inputs, not automatic PASS inheritance.

## Result routing

If visual inspection finds a real implementation defect:

```text
ENGINEERING_VISUAL_CONFORMANCE=FAIL
ENGINEERING_REPAIR_REQUIRED=YES
NEW_CANDIDATE_SHA=REQUIRED_AFTER_REPAIR
ALL_REQUIRED_EXACT_SHA_EVIDENCE_REGENERATED=YES
```

If visual inspection passes without candidate mutation:

```text
ENGINEERING_VISUAL_CONFORMANCE=PASS
FRESH_ATOMIC_ENGINEERING_READY=REQUIRED
NEXT_AUTHORITY=PRODUCT_GOVERNANCE_CANDIDATE_ADMISSION
```

## Historical rule changes

If the visual evidence rule is added after a prior Engineering Ready through an approved Change Request/addendum, do not rewrite the prior terminal as invalid at issuance solely because the new rule is stricter. Perform a fresh independent Engineering re-entry for further progression.

## Non-equivalence

```text
LOCAL_AGENT_OBSERVATION
!= ENGINEERING_ADJUDICATION
ENGINEERING_VISUAL_CONFORMANCE_PASS
!= PRODUCT_EXPERIENCE_PASS
!= DEMO_RETURN_ACCEPTED
!= HUMAN_OWNER_ACCEPTED
!= RELEASE_AUTHORIZED
```
