# Expense Tracker Web Application

A simple and user-friendly web application for managing personal expenses, tracking spending, and viewing expense summaries through a dashboard.

## 📌 Project Overview

The **Expense Tracker Web Application** is a full-stack web application developed using **Python Flask, HTML, CSS, and JavaScript**.

The application allows users to create and manage users, add and update expenses, delete expenses, and view spending analytics through a simple dashboard.

Expense data is stored locally using a JSON-based persistence layer.

## 🚀 Key Features

* 👤 Create and manage users
* 🔄 Select and switch between active users
* ➕ Add new expenses
* ✏️ Edit existing expenses
* 🗑️ Delete expenses
* 🔐 Prevent users from modifying another user's expenses
* ✅ Input validation and error handling
* 📊 Dashboard with:

  * Total expenses
  * Average expense
  * Category-wise spending
* 📭 Handles users with zero expenses
* 💾 Local JSON-based data persistence
* 📱 Responsive and simple user interface

## 🛠️ Tech Stack

| Technology | Purpose                       |
| ---------- | ----------------------------- |
| Python     | Backend programming           |
| Flask      | Web application framework     |
| HTML5      | Frontend structure            |
| CSS3       | Styling and responsive design |
| JavaScript | Frontend functionality        |
| JSON       | Local data persistence        |

## 📂 Project Structure

```text
Expense Tracker Web Application/
│
├── backend/
│   └── app.py
│
├── frontend/
│   ├── templates/
│   │   └── index.html
│   └── static/
│       ├── app.js
│       └── styles.css
│
├── database/
│   └── data.json
│
├── tests/
│   ├── acceptance-validation.md
│   ├── defect-log.md
│   ├── edge-case-validation.md
│   └── phase-7-test-execution.md
│
├── screenshots/
│
├── docs/
│
├── requirements.txt
├── phase-7-implementation-report.md
├── phase-7-implementation-report.pdf
├── .gitignore
└── README.md
```

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/priyadharshini2004deee-cyber/expense-tracker-phase-7.git
```

### 2. Navigate to the project directory

```bash
cd expense-tracker-phase-7
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```bash
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the Flask application:

```bash
python backend/app.py
```

Then open the following URL in your browser:

```text
http://127.0.0.1:5000
```

## 📊 Application Workflow

```text
Create / Select User
        ↓
Add Expense
        ↓
Validate Expense
        ↓
Save Expense
        ↓
View / Edit / Delete
        ↓
Dashboard Analytics
        ↓
Category-wise Spending
```

## 🧪 Testing & Validation

The project includes documented test scenarios covering:

* User creation
* Duplicate user handling
* Expense creation
* Expense editing
* Expense deletion
* Input validation
* User ownership protection
* Dashboard calculations
* Category-wise expense summaries
* Zero-expense scenarios
* Edge cases and validation scenarios

Detailed test documentation is available in the `tests/` directory.

> **Note:** Test documentation is included in the repository. Runtime test execution status should be verified before claiming all test cases as passed.

## 📸 Screenshots

Application screenshots are available in the `screenshots/` directory.

## 📚 Documentation

Additional project documentation is available in:

* `docs/`
* `phase-7-implementation-report.md`
* `phase-7-implementation-report.pdf`

## 🔮 Future Enhancements

Possible future improvements include:

* User authentication and login
* Database integration using SQLite/PostgreSQL
* Expense filtering and search
* Export expenses to CSV/Excel
* Monthly and yearly spending reports
* Data visualization using charts
* Recurring expense management
* Cloud deployment
* REST API integration

## 💡 What I Learned

Through this project, I gained practical experience in:

* Building a Flask-based web application
* Connecting frontend and backend components
* Working with REST-style API endpoints
* Handling CRUD operations
* Implementing input validation
* Managing local data persistence
* Designing dashboard-based analytics
* Structuring a full-stack project
* Using Git and GitHub for version control

## 👩‍💻 Author

**Priyadharshini**

AI/ML Fresher | Python Developer | Data Analyst

### GitHub

`priyadharshini2004deee-cyber`

---

⭐ If you find this project useful, feel free to explore the repository and its documentation.
