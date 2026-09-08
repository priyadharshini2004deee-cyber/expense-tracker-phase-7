# AI Prompts Used — Phase 7

## Purpose
This document records the main AI-assisted development prompts used during the Phase 7 Expense Tracker implementation. AI was used as a development and reasoning aid; generated output was reviewed, adapted and manually validated.

## Prompt 1 — Requirement Understanding
**Purpose:** Convert the assessment requirements into an implementation-oriented checklist.

**Prompt:**
> Analyse the Expense Tracker assessment requirements. Identify the mandatory features, business rules, validations, edge cases, deliverables, assumptions and out-of-scope items. Do not invent requirements that are not supported by the assessment.

**Review / Use:** The output was used as a planning aid and was reviewed against the supplied assessment requirements.

## Prompt 2 — Application Architecture
**Purpose:** Define a simple implementation suitable for the assessment scope.

**Prompt:**
> Propose a simple architecture for a basic Expense Tracker web application using Python, Flask, HTML, CSS and Vanilla JavaScript with local JSON persistence. Keep the design minimal and aligned to the mandatory assessment scope. Identify backend, frontend, persistence and validation responsibilities.

**Review / Use:** The proposed structure was reviewed and kept intentionally simple for the assessment.

## Prompt 3 — User Management
**Purpose:** Implement user creation, duplicate handling and active-user selection.

**Prompt:**
> Design and implement user creation and active-user selection for the Expense Tracker. Include duplicate-name handling and validation. Keep users and expenses scoped correctly.

**Review / Use:** The generated approach was reviewed before use and manually tested through the application.

## Prompt 4 — Expense CRUD
**Purpose:** Implement expense create, edit and delete functionality.

**Prompt:**
> Implement Expense Tracker CRUD operations for create, edit and delete. Validate amount, date, category and description before saving. Ensure editing validates before changing stored data.

**Review / Use:** CRUD behaviour was manually demonstrated and validated.

## Prompt 5 — Business Validation
**Purpose:** Identify negative and edge-case validations.

**Prompt:**
> Review the Expense Tracker validation logic and identify negative and edge cases for amount, date, category, description, duplicate users, missing active user and invalid edits. Provide expected business-level validation messages.

**Review / Use:** The validation behaviour was manually tested, including negative amount, zero amount and empty description.

## Prompt 6 — Dashboard
**Purpose:** Implement and review dashboard calculations.

**Prompt:**
> Implement the Expense Tracker dashboard for the active user. Calculate total expense, average expense, valid expense count and category breakdown. Define correct zero-expense behaviour.

**Review / Use:** Dashboard totals, average, valid count and category breakdown were checked during the demonstration.

## Prompt 7 — Testing
**Purpose:** Generate functional, negative and edge-case test ideas.

**Prompt:**
> Create functional, negative and edge-case test cases for the Expense Tracker. Include expected results, validation scenarios, CRUD operations, dashboard calculations, user ownership and persistence. Do not mark tests as passed unless they are actually executed.

**Review / Use:** The resulting test ideas were used as a QA planning aid. Actual execution status was recorded separately in the test execution document.

## Prompt 8 — Code / Logic Review
**Purpose:** Review AI-generated implementation for logical gaps.

**Prompt:**
> Review the Expense Tracker implementation for logical errors, missing validation, ownership issues, incorrect dashboard calculations, persistence problems and edge cases. Explain each issue and propose a minimal correction without adding unnecessary features.

**Review / Use:** Suggestions were reviewed before changes were retained.

## Prompt 9 — Scope Control
**Purpose:** Prevent unnecessary features from expanding the assessment scope.

**Prompt:**
> Review the proposed Expense Tracker features against the assessment scope. Separate mandatory requirements, clarification-dependent items, optional items and out-of-scope features. Do not add features merely because they are common in expense applications.

**Review / Use:** This supported the documented scope exclusions such as multi-currency, export, forecasting, bank integration, OCR, notifications, recurring expenses and RBAC.

## AI Output Review Approach
AI-generated outputs were treated as suggestions rather than automatically accepted code. The implementation was reviewed for:
- Requirement alignment
- Validation correctness
- Data ownership
- Dashboard calculation correctness
- Persistence behaviour
- Edge cases
- Scope control
- Testability

The final behaviour was manually exercised in the local web application. The test execution document records the scenarios actually demonstrated.
