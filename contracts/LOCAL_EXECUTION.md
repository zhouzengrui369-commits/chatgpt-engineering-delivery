# Local Agent Execution Request and Observation Receipt

The only authorized local-execution role is an Owner-designated Local Agent. Engineering Delivery and Product Governance may issue the request according to the frozen evidence owner, but neither role performs the local steps itself.

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
authorized_executor: OWNER_DESIGNATED_LOCAL_AGENT
local_agent_context_id: ""
prescribed_steps: []
allowed_data: []
forbidden_data: []
source_mutation: FORBIDDEN
test_mutation: FORBIDDEN
commit_push: FORBIDDEN
self_repair: FORBIDDEN
scope_expansion: FORBIDDEN
```

## Observation receipt — issued by Local Agent

```yaml
protocol_version: DELIVERY-LIFECYCLE-1.0
actor_role: LOCAL_EXECUTOR
executor_type: OWNER_DESIGNATED_LOCAL_AGENT
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

The Local Agent reports observations only. The role owning the evidence bucket adjudicates those observations.

Normal repository CI is separate technical evidence. It cannot substitute for a required Local Agent receipt when the contract requires Owner-machine credentials, native runtime, local database, real device/data/browser, or local deployment observations.

Historical receipts from retired executor topologies remain immutable for their original exact SHA/gate and do not authorize future local execution.
