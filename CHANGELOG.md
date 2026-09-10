# Changelog

## 0.2.2-alpha — 2026-09-10

- Add Human Owner ecosystem visual-evidence authority `knowme-ecosystem#39`.
- Require visual-product Engineering Ready to include human-reviewable visual evidence plus Engineering personal inspection of the actual evidence bytes.
- Add `core/VISUAL_EVIDENCE_POLICY.md`.
- Extend Local Agent request/receipt contracts with visual bundle refs, paired screenshots, interaction captures, dynamic evidence, difference index, SHA256 integrity manifest and source/test/runtime mapping.
- Keep Local Agent visual adjudication `PENDING`; only Engineering Delivery may issue the Engineering visual `PASS|FAIL` conclusion.
- Forbid text-only screenshot/gate receipts from satisfying the visual Engineering Ready gate.
- Preserve historical Engineering terminals under the evidence rules effective when they were issued.

## 0.2.1-alpha — 2026-09-08/09

- Standardize Owner-designated Local Agent as sole local executor.
- Require post-deployment operational/browser verification after local deployment/runtime materialization.
- Keep Engineering Delivery off the Owner-machine execution path.

## 0.2.0-alpha

- Role-separated Engineering Delivery lifecycle baseline and atomic Engineering Ready package.
