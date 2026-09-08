# Ecosystem Execution Topology Policy — Engineering Delivery

Status: HUMAN-OWNER SUCCESSOR POLICY
Protocol: `DELIVERY-LIFECYCLE-1.0`

```text
GITHUB=CONTROL_PLANE_ONLY
GITHUB_HOSTED_RUNNER=FORBIDDEN
SELF_HOSTED_RUNNER=FORBIDDEN
ANY_GITHUB_ACTIONS_RUNNER_AS_PROJECT_EXECUTOR=FORBIDDEN
LOCAL_EXECUTOR=LOCAL_AGENT
LOCAL_DEPLOYMENT=LOCAL_AGENT_ONLY
LOCAL_TECHNICAL_TEST_EXECUTION=LOCAL_AGENT
SILENT_FALLBACK=FORBIDDEN
```

`LOCAL_AGENT` is the canonical project execution role. There is no separate `OWNER_AUTHORIZED_LOCAL_AGENT` lifecycle role. Historical receipts using that phrase remain historical evidence only.

Engineering Delivery owns technical design, source/tests, commit/push/PR, exact candidate construction, technical remediation, Candidate Manifest and Technical Receipt. When execution is needed, Engineering Delivery issues a bounded Local Agent execution contract and adjudicates the sanitized receipt.

`CI` means the repeatable contracted technical gate set. It does not imply GitHub Actions. GitHub stores control-plane state and evidence refs; it is not the project execution plane.

Local Agent may materialize exact SHA, install dependencies, build, run technical tests, start/deploy locally, execute prescribed runtime/device/data/browser checks, configure the local runtime and return sanitized observations.

## Local runtime credential mechanics

Local runtime-only technical configuration belongs to Engineering Delivery + Local Agent unless the operation crosses a true Human Owner authority boundary.

Engineering Delivery may require a locally generated secret (for example a random JWT signing secret) when the exact candidate requires it. Local Agent may generate and persist that value locally without a separate Human Owner confirmation when all of the following are true:

- the secret is only for the local runtime under the current Engineering contract;
- it does not grant new access to an external account/provider;
- it does not authorize payment, production release/deployment or irreversible action;
- it is not printed, exported, committed, uploaded to GitHub or returned in the receipt.

The receipt records only non-secret facts such as `LOCAL_RUNTIME_SECRET_PRESENT=YES`, strength/format compliance, and `SECRET_VALUE_EXPORTED=false`.

Human Owner authority remains required for actual major product trade-offs, new external-account/provider credentials or permissions, payment/billing decisions, production credentials/production authorization, destructive/irreversible actions and final Human Owner Acceptance.

Do not elevate ordinary local runtime configuration into `BLOCKED_EXTERNAL_AUTHORITY` merely because the value is secret.

Local Agent must not modify source/tests, commit/push, self-repair, expand scope, declare Engineering Ready, admit a candidate, issue Product Experience, grant Owner Acceptance, merge or release.

Historical Runner evidence remains immutable for its original context but has no prospective execution authority.

Any project whose frozen contract explicitly requires GitHub Actions/Runner execution must receive a Product Governance Change Request and successor contract before the execution path changes. Engineering must not silently weaken the technical gate; it changes only the execution surface while preserving commands, coverage, identity and receipt requirements.

FORBIDDEN_CLAIMS_ACKNOWLEDGED=YES
