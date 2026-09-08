# Known Issues / Limitations — Phase 7

## 1. Phase 1–6 Traceability Limitation
The complete approved Phase 1–6 source documents were not available in the final implementation build context. Therefore, exact one-to-one mappings for BR, V, AC, EC and TC identifiers are not asserted where the source wording could not be verified.

## 2. Full Phase 8 QA Not Completed
The controlled TC-001–TC-065 test records remain Not Run / Pending Evidence where the exact approved Phase 1–6 scenario wording and mappings were not available for verification.

A focused set of manually demonstrated scenarios is documented separately in `tests/phase-7-test-execution.md`. No unexecuted controlled test case is claimed as Passed.

## 3. Authentication
Authentication is treated as clarification-dependent / outside the mandatory baseline. The Phase 7 implementation therefore does not claim a login, password, session-security or identity-verification workflow.

## 4. Optional / Clarification-Dependent Features
Payment Method and Dashboard Filters are not treated as mandatory baseline features.

## 5. Local JSON Persistence
The application uses local JSON persistence for the Phase 7 implementation. Its classification as a confirmed requirement versus a working implementation assumption requires verification against the approved Phase 1–6 documents.

## 6. Advanced Features Not Implemented
The following are intentionally outside the implemented baseline unless separately approved:
- Multi-currency
- Expense export
- Forecasting
- Bank integration
- OCR / receipt scanning
- Notifications
- Recurring expenses
- RBAC
- Complex audit trails
- Soft delete / undo
- Other unapproved advanced features

## 7. Evidence Limitation
The final submission should include the available demo video and screenshots captured during actual execution. Evidence should only be used to support scenarios that were actually demonstrated.

## 8. Defect Status
No fabricated defects or Pass results are included. Any future issue discovered during broader QA should be recorded with a defect reference and retested after correction.

## 9. Scope-Control Statement
These limitations are intentional scope controls and do not represent missing mandatory functionality unless the approved Phase 1–6 requirements explicitly establish otherwise.

## Final Note
The application is demonstration-ready for the implemented Phase 7 baseline. Remaining limitations and unverified requirements are explicitly documented rather than being presented as completed functionality.
