# Phase 7 — Application Development & Controlled Implementation

**Project:** Expense Tracker Web Application  
**Assessment:** Navia Markets Limited — Executive Project Coordinator

## A. Implementation Summary
A working Flask-based Expense Tracker application has been generated from the supplied Phase 7 baseline. It implements user management, active-user selection, expense lifecycle, validation, ownership controls, dashboard calculations and local persistence.

**Application Status:** Implemented  
**Execution Verification:** Pending Evidence  
**QA Status:** Pending Execution  
**Acceptance Status:** Pending Execution

The application is not being declared accepted or released.

## B. Technology Stack
- Python 3
- Flask
- HTML5
- CSS
- Vanilla JavaScript
- JSON file persistence

The stack is lightweight and suitable for a local assessment demonstration.

## C. Project Structure
The project contains backend logic, frontend assets, JSON persistence, test-control documents, evidence structure, documentation and the Phase 7 report.

## D. Implemented Features
- User creation
- User-name normalization and validation
- Case-insensitive duplicate-user handling
- Active-user selection
- No-active-user behaviour
- Expense creation
- Required-field validation
- Amount validation: numeric and greater than zero
- Date validation for valid calendar dates
- Required category and description
- Expense ownership
- Active-user scoped expense list
- Ownership verification during edit/delete
- Expense editing
- Invalid-edit protection
- Expense deletion with confirmation
- Total Expense
- Average Expense
- Category Breakdown
- Active-user dashboard scope
- Zero-expense behaviour
- Local user/expense/ownership persistence
- Business-level validation messages

## E. Validation Implementation
The application rejects blank/duplicate users, missing active user, missing or invalid amounts, non-positive amounts, invalid dates, missing categories and missing descriptions. Edit/delete operations are ownership-scoped.

No unsupported category allow-list or description maximum is imposed.

**Requires Clarification / Verification:** exact approved category list, future-date policy, description boundary and any other precise validation constraint not present in the supplied build context.

## F. Ownership / Data Integrity Controls
Expenses store a user identifier. Normal list, edit, delete and dashboard operations are scoped to the active user. Edit validation occurs before mutation so a failed edit does not intentionally overwrite the previous valid record.

This is business-level ownership control. Authentication, RBAC and enterprise authorization are not implemented.

## G. Dashboard Calculation Implementation
**Total Expense** = sum of valid expenses belonging to the active user.

**Average Expense** = Total Expense / number of valid expenses belonging to the active user.

**Category Breakdown** = category totals from valid expenses belonging to the active user.

With zero valid expenses, total and average are zero and the UI displays an empty state.

## H. Persistence Implementation
Users, expenses and ownership are stored in `database/data.json`.

**Baseline qualification:** whether persistence is a confirmed Navia requirement or a Phase 2 working assumption must be verified against the controlled Phase 1–6 documents.

## I. Development Task Status
The requested DEV-001–DEV-038 identifiers are preserved. Exact BR/V/AC/EC/TC mappings are not guessed.

| DEV-001 | User creation | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-002 | User-name validation | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-003 | Duplicate handling | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-004 | Active-user selection | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-005 | No-user / no-active-user behaviour | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-006 | Required expense fields | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-007 | Amount validation | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-008 | Date validation | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-009 | Category validation | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-010 | Description validation | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-011 | Ownership assignment and protection | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-012 | Invalid-record prevention | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-013 | Existing expense selection | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-014 | Ownership verification during editing | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-015 | Valid expense editing | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-016 | Invalid-edit protection | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-017 | Correct expense targeting | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-018 | Ownership protection during deletion | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-019 | Approved confirmation/cancellation behaviour | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-020 | Permanent deletion behaviour where applicable | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-021 | Total Expense calculation | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-022 | Average Expense calculation | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-023 | Category Breakdown | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-024 | Active-user dashboard scope | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-025 | Zero-expense behaviour | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-026 | Invalid-record exclusion | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-027 | User persistence | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-028 | Expense persistence | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-029 | Ownership persistence | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-030 | Normal restart behaviour | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-031 | Loss/duplication prevention | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-032 | Business validation messages | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-033 | Preservation of valid records after failed operations | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-034 | Implementation evidence/control | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-035 | Phase 8 test readiness | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-036 | Acceptance evidence readiness | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-037 | Scope control | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |
| DEV-038 | Final implementation review | Controlled implementation task | Requires Clarification / Verification | Pending Evidence |

## J. Known Assumptions
1. JSON is used as the local persistence mechanism.
2. Ownership is enforced at business-logic level without authentication.
3. Category is required but no unsupported fixed category list is imposed.
4. No unsupported description maximum is imposed.

## K. Clarifications Required
- Exact one-to-one BR/V/AC/EC/TC mappings from the approved Phase 1–6 documents.
- Exact category validation list, if specified.
- Exact future-date treatment, if specified.
- Exact description boundary, if specified.
- Exact deletion confirmation/cancellation wording, if specified.
- Confirmation of persistence classification.
- Authentication remains clarification-dependent/outside the mandatory baseline.

## L. Optional Features
- Payment Method — optional/non-mandatory; not implemented.
- Dashboard Filters — optional/non-mandatory; not implemented. EC-020 remains controlled.

## M. Out-of-Scope Features
Not implemented:
- Multi-currency
- Export
- Forecasting
- Bank integration
- OCR
- Notifications
- Recurring expenses
- RBAC
- Complex audit trails
- Soft delete / undo
- Authentication as a mandatory feature

## N. Implementation Evidence Available
- Complete source-code project
- Persistence file
- Documentation
- QA/defect/acceptance/edge-case control files
- Python syntax compilation check
- Successful local runtime execution at `http://127.0.0.1:5000`
- Manual functional and negative validation evidence
- Demo video recording

**Evidence Status:** Local runtime execution and demonstration evidence completed. Screenshot evidence should be retained with the final submission package where available.

## O. Known Limitations
- Full Phase 1–6 source documents were not attached to the build context, so exact identifier mappings cannot be asserted.
- Full Phase 8 QA has not been performed; therefore this report does not claim that all TC-001–TC-065, EC-001–EC-020 and AC-001–AC-016 scenarios have been executed.
- Manual demonstration covered user creation/selection, expense creation, editing, deletion, dashboard calculations, negative amount validation, zero amount validation, empty-description validation and persistence after refresh.
- Authentication, RBAC and other explicitly out-of-scope or clarification-dependent features remain unimplemented.
- Screenshot evidence should be included in the final submission where required.

## P. Phase 8 QA Readiness
The application is structured for TC-001–TC-065, EC-001–EC-020 and AC-001–AC-016. A focused local demonstration and validation pass has been completed. The remaining Phase 8 baseline scenarios should continue to be tracked as Not Run / Pending Execution unless independently executed and evidenced.

## Q. Recommended Next Step
Include the completed demo video and available screenshots/evidence in the final submission. If time permits, continue the broader Phase 8 QA baseline, capture evidence, log/retest defects and update acceptance validation.

## Baseline Control
Preserved exactly:
- BR-001–BR-057
- V-001–V-040
- AC-001–AC-016
- EC-001–EC-020
- TC-001–TC-065
- DEV-001–DEV-038

Where exact mapping cannot be verified: **Requires Clarification / Verification**.

## Final Control Statement
Phase 7 implements the supplied baseline. It does not replace earlier phases, convert assumptions into confirmed requirements, or declare QA passed, accepted or released.