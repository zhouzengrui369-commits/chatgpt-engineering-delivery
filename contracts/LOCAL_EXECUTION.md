# Local Execution Request and Observation Receipt

## Request — issued by Engineering Delivery or Product Governance according to the frozen evidence owner

```yaml
protocol_version: DELIVERY-LIFECYCLE-1.0
goal_id: ""
milestone_id: ""
requesting_role: ENGINEERING_DELIVERY | PRODUCT_GOVERNANCE
evidence_bucket: engineering_required | admission_required | review_required
repository: ""
candidate_sha: ""
candidate_tree: ""
authorized_executor: ""
prescribed_steps: []
allowed_data: []
forbidden_data: []
source_mutation: FORBIDDEN
test_mutation: FORBIDDEN
commit_push: FORBIDDEN
self_repair: FORBIDDEN
scope_expansion: FORBIDDEN
```

## Observation receipt — issued by Local Executor

```yaml
protocol_version: DELIVERY-LIFECYCLE-1.0
actor_role: LOCAL_EXECUTOR
actor_context_id: ""
goal_id: ""
milestone_id: ""
candidate_sha: ""
candidate_tree: ""
materialization_identity: ""
observations: []
sanitized_evidence_refs: []
source_mutation: NO
test_mutation: NO
commit_push: NO
self_repair: NO
scope_expansion: NO
verdict_claimed: NONE
issued_at: ""
```

The Local Executor reports observations only. The role owning the evidence bucket adjudicates those observations.
