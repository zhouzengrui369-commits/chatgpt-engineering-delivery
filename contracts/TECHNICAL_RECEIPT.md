# Technical Receipt

The Technical Receipt records Engineering Delivery's technical adjudication for one exact candidate.

```yaml
protocol_version: DELIVERY-LIFECYCLE-1.0
actor_role: ENGINEERING_DELIVERY
actor_context_id: ""

goal_id: GOAL-XXX
milestone_id: MILESTONE-GOAL-XXX
product_contract_commit: ""
engineering_delivery_contract_ref: ""

candidate_sha: ""
candidate_tree: ""
candidate_parent: ""
branch_head_match: false
pr_head_match: false
worktree_clean: false

commands: []
tests:
  passed: []
  failed: []
  not_run: []
ci_runs: []
builds: []
migrations: []
security_and_privacy_checks: []
technical_code_review: ""
diff_scope_check: ""

engineering_required_evidence:
  status: COMPLETE | INCOMPLETE
  items: []
local_executor_observations:
  receipts: []
  engineering_adjudication: []

admission_required_evidence:
  status: OPEN | COMPLETE
  items: []
review_required_evidence:
  status: OPEN | COMPLETE
  items: []
open_non_engineering_gates: []

source_dirty: false
credentials_exposed: false
unapproved_deviations: []
known_defects: []
known_limitations: []
artifacts: []

engineering_delivery_result: ENGINEERING_READY | ENGINEERING_NOT_READY | BLOCKED_CHANGE_REQUEST_REQUIRED | BLOCKED_EXTERNAL_AUTHORITY | BLOCKED_IDENTITY_DRIFT
engineering_ready: YES | NO
first_blocker: ""
recommended_next_gate: PRODUCT_GOVERNANCE_CANDIDATE_ADMISSION
forbidden_claims_acknowledged: true
issued_at: ""
```
