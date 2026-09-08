# Expense Tracker Web Application — Phase 7

## Overview
Controlled Phase 7 implementation for the Navia Markets Limited Executive Project Coordinator assessment.

## Technology
Python 3, Flask, HTML5, CSS, Vanilla JavaScript and JSON file persistence.

## Core Features
- User creation and duplicate handling
- Active-user selection
- Expense create/edit/delete
- Amount/date/category/description validation
- Ownership protection
- Dashboard total, average and category breakdown
- Zero-expense behaviour
- Local persistence
- Business-level validation messages

## Scope Control
**Optional/non-mandatory:** Payment Method, Dashboard Filters.

**Clarification-dependent/outside mandatory baseline:** Authentication.

**Out of scope:** Multi-currency, export, forecasting, bank integration, OCR, notifications, recurring expenses, RBAC, complex audit trails, soft delete/undo and other unapproved features.

## Structure
```text
expense-tracker-phase-7/
├── backend/app.py
├── frontend/templates/index.html
├── frontend/static/app.js
├── frontend/static/styles.css
├── database/data.json
├── tests/
├── screenshots/
├── docs/
├── README.md
├── requirements.txt
└── phase-7-implementation-report.md
```

## Setup
```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
# source .venv/bin/activate
pip install -r requirements.txt
```

## Run
```bash
python backend/app.py
```
Open `http://127.0.0.1:5000`.

## Usage
Create a user, select the active user, create expenses, edit/delete them, switch users and review user-scoped dashboard calculations. Restart the application to observe local persistence.

## Validation
Blank/duplicate user names, missing active user, invalid/non-positive amounts, invalid dates, missing category and missing description are rejected. Failed edits validate before modifying the stored record.

## Dashboard
Total = sum of valid active-user expenses.

Average = total divided by valid active-user expense count.

Category Breakdown = category totals from valid active-user expenses.

Zero valid expenses produce zero total, zero average and an empty-state message.

## Persistence
`database/data.json` stores users, expenses and ownership. Its classification as a confirmed requirement versus Phase 2 working assumption requires verification against the approved Phase 1–6 documents.

## QA
`tests/phase-7-test-execution.md` preserves TC-001–TC-065 and marks them Not Run. Acceptance and edge-case documents preserve AC-001–AC-016 and EC-001–EC-020.

## Source-Control Note
The complete Phase 1–6 source documents were not attached to the implementation build context. Exact BR/V/AC/EC/TC wording and mappings are therefore not guessed.

## Demonstration
Show user creation, active-user selection, validation messages, expense create/edit/delete, dashboard calculations, user-scoped records, zero-expense state and persistence after restart.

## Verification Status
The source code has been syntax-checked. Runtime execution and screenshot evidence are **Pending Evidence** in the current generation environment. Do not report tests as Passed until Phase 8 execution is actually performed.
