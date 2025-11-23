# Personal Expense Tracker

# 💰 Python Console Expense Tracker

This is a simple, menu-driven command-line application built in Python for tracking personal or small-scale expenses. It uses a **list of dictionaries** to store expense records, ensuring no entries are overwritten when recording multiple transactions under the same category.

## ✨ Features

  * **Add Expense:** Record new financial transactions with details like category, date, description, and amount.
  * **View All Expenses:** Display a detailed, formatted list of every recorded expense.
  * **Total Expenses:** Calculate and display the grand total of all money spent.
  * **Category-wise Summary:** Provides a breakdown of total spending for each unique expense category.

## 🚀 Getting Started

### Prerequisites

You need **Python 3.x** installed on your system.

### Installation and Setup

1.  Save the Python code provided (the version that uses `expense = []`) into a file named, for example, `expense_tracker.py`.
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.

### How to Run

Execute the script using the Python interpreter:

```bash
python expense_tracker.py
```

## 🛠️ Usage

When you run the script, the main menu will appear:

```
===============================
💰 Simple Console Expense Tracker
===============================
1. Add Expense
2. View All Expenses (Detailed)
3. Total Expenses (Grand Total)
4. Category-wise Summary
5. Exit
===============================

Enter your choice (1-5):
```

### 1\. Add Expense

You will be prompted for:

  * **Category** (e.g., *Groceries*, *Fuel*, *Rent*)
  * **Date** (Recommended format: `DD-MM-YYYY`)
  * **Description**
  * **Amount** (Must be a positive number)

### 2\. View All Expenses (Detailed)

This option displays all recorded transactions in a readable table format.

### 3\. Total Expenses (Grand Total)

This calculates and displays the sum of all recorded amounts (e.g., `Total Money Spent: ₹1500.50`).

### 4\. Category-wise Summary

This provides an itemized list showing the total money spent for each distinct category (e.g., `Food: ₹450.00`, `Utilities: ₹600.00`).

## 💡 Code Structure Overview

The application is built around a main list, `expense`, which holds dictionaries for each transaction:

```python
expense = [
    {
        "Category": "Food",
        "Date": "23-11-2025",
        "Description": "Coffee shop",
        "Amount": 150.00
    },
    # ... more expense dictionaries
]
```

This structure is robust, ensuring that the history of all transactions is preserved.

## 🤝 Contribution

Feel free to suggest enhancements or fork the repository to add features like data persistence (saving to a file) or more advanced reporting.

