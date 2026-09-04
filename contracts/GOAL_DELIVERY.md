# Engineering Goal Delivery Contract

The Product Governance handoff must classify evidence ownership before Engineering Delivery starts.

```yaml
protocol_version: DELIVERY-LIFECYCLE-1.0
goal_id: GOAL-XXX
milestone_id: MILESTONE-GOAL-XXX
relationship: ONE_GOAL_EQUALS_ONE_MILESTONE

product_baseline_ref: ""
product_contract:
  commit: ""
  tree: ""
  path: ""

engineering_delivery_authority:
  repository: zhouzengrui369-commits/chatgpt-engineering-delivery
  commit: ""
  tree: ""
  skill_path: core/ENGINEERING_DELIVERY_SKILL.md

engineering_delivery_contract_ref: ""
input_repository: owner/repo
input_branch: ""
input_sha: ""
input_tree: ""
input_parent: ""
engineering_branch: ""
engineering_pr: ""

allowed_paths: []
forbidden_paths: []
in_scope_outcomes: []
out_of_scope: []
approved_change_requests: []

evidence_ownership:
  engineering_required: []
  admission_required: []
  review_required: []
  product_experience: []
  human_owner: []

required_candidate_artifacts:
  - candidate_manifest
  - technical_receipt

local_executor:
  required: false
  authorized_executor: ""
  mutation_forbidden: true
  observation_only: true

engineering_terminal_state: PENDING
```

Missing evidence classification is a blocking contract ambiguity. Engineering Delivery must not decide which later gate owns an unclassified requirement.
