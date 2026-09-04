# Candidate Manifest

The manifest is the immutable identity and scope declaration for one Engineering Delivery candidate. It is not Candidate Admission or Product Experience acceptance.

```yaml
protocol_version: DELIVERY-LIFECYCLE-1.0
actor_role: ENGINEERING_DELIVERY
actor_context_id: ""

goal_id: GOAL-XXX
milestone_id: MILESTONE-GOAL-XXX
relationship: ONE_GOAL_EQUALS_ONE_MILESTONE

product_contract:
  commit: ""
  tree: ""
  path: ""
engineering_delivery_contract_ref: ""

repository: owner/repo
pr: ""
branch: ""
candidate_sha: ""
candidate_tree: ""
candidate_parent: ""
branch_head_match: false
pr_head_match: false
worktree_clean: false

implemented_scope: []
not_implemented: []
diff_inventory: []
known_defects: []
known_limitations: []
known_deviations: []
unapproved_deviations: []
approved_change_requests: []

evidence_ownership:
  engineering_required:
    status: INCOMPLETE
    refs: []
  admission_required:
    status: OPEN
    refs: []
  review_required:
    status: OPEN
    refs: []
  product_experience:
    status: NOT_RUN
  human_owner:
    status: NOT_RUN

technical_receipt_ref: ""
local_execution_receipts: []
open_non_engineering_gates: []

engineering_ready: YES | NO
recommended_next_gate: PRODUCT_GOVERNANCE_CANDIDATE_ADMISSION

forbidden_claims_acknowledged: true
forbidden_claims:
  - CANDIDATE_ADMITTED
  - PRODUCT_REVIEW_ELIGIBLE
  - PRODUCT_EXPERIENCE_PASS
  - HUMAN_OWNER_ACCEPTED
  - MERGE_AUTHORIZED
  - RELEASE_AUTHORIZED
  - GOAL_MILESTONE_CLOSED

issued_at: ""
```
