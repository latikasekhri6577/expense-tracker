# 💰 Personal Expense Tracker

A lightweight, command-line interface (CLI) Python application designed to help users log, track, manage, and analyze their daily financial expenses. The application stores data locally using a persistent JSON file format.

---

## ✨ Features

* **Log Expenses:** Quickly record amounts, categories, and descriptions. Dates are automatically logged using your local system time.
* **Smart Search Engine:** Filter your historical transactions by specific categories, explicit dates (`dd/mm/yy`), or text keywords inside descriptions.
* **Financial Analytics:** 
  * Calculate the grand total of all logged transactions instantly.
  * Generate aggregate, category-wise spending reports to see exactly where your money goes.
* **Persistent Data Storage:** Automatically loads historical logs upon startup and safely updates your local `expensesRecords.json` file whenever you save or exit.
* **Robust Error Handling:** Built-in validation safeguards the application against invalid numeric inputs or missing data files.

---

## 🛠️ Tech Stack & Requirements

* **Language:** Python 3.x
* **Core Modules Used:** `datetime`, `json` (No external third-party dependencies required)

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3 installed on your local machine. You can verify this by running:
```bash
python --version
```

### 2. Installation
Clone this repository or download the source script files directly:
```bash
git clone https://github.com
cd expense-tracker
```

### 3. Running the Application
Launch the tool by executing the main script file via your terminal or command prompt:
```bash
python main.py
```

---

## 📖 How To Use

When launched, the interactive CLI menu will display the following operational pathways:

```text
--- Expense Tracker Menu ---
1. Add expense
2. Search expenses
3. Calculate total
4. Category-wise spending
5. Save expenses
6. Exit
```

1. **Adding Data:** Select `1` and type your category (e.g., *Food*), amount (e.g., *14.50*), and a brief description.
2. **Reviewing Data:** Select `2` to look up specific entries using sub-filters.
3. **Data Integrity:** While option `5` manually backs up data, selecting option `6` safely auto-saves your progress before terminating the runtime process.

---

## 📂 File Architecture

* `main.py` - Contains the foundational runtime loops, system menu layouts, input parsing, and operational functions.
* `expensesRecords.json` - Generated automatically during runtime to store data logs persistently across individual usage sessions.

---

## 📝 License
This project is open-source and available under the [MIT License](LICENSE).
