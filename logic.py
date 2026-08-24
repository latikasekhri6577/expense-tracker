from datetime import date
import json

def show_menu():
    print("\n--- Expense Tracker Menu ---")
    print("1. Add expense")
    print("2. Search expenses")
    print("3. Calculate total")
    print("4. Category-wise spending")
    print("5. Save expenses")
    print("6. Exit")

def add_expense(expenses):
    category = input("Enter category: ").strip()
    
    # Input validation to prevent crashes on non-numeric input
    try:
        amt = float(input("Enter amount spent: "))
    except ValueError:
        print("Invalid amount! Please enter a number.")
        return

    description = input("Enter description: ").strip()
    
    expense = {
        "id": len(expenses) + 1,
        "date_spent": date.today().strftime("%d/%m/%y"),
        "category": category,
        "amount": amt,
        "description": description
    }
    expenses.append(expense)
    print("Expense added successfully!")

def search_expenses(expenses):
    if not expenses:
        print("No expense records available to search.")
        return

    print("Search by: 1. Category  2. Date  3. Description keyword")
    sub_choice = input("Enter choice: ")
    results = []
          
    if sub_choice == "1":
        query = input("Enter category: ").strip().lower()
        results = [e for e in expenses if e['category'].lower() == query] 

    elif sub_choice == "2":
        query = input("Enter date (dd/mm/yy): ").strip()
        results = [e for e in expenses if e['date_spent'] == query] # Fixed key name

    elif sub_choice == "3":
        query = input("Enter keyword to search in description: ").strip().lower()
        results = [e for e in expenses if query in e['description'].lower()]

    else:
        print("Invalid choice")
        return

    if not results:
        print("No matching expenses found.")
    else:
        print("\n--- Search Results ---")
        for e in results:
            print(f"ID: {e['id']} | Date: {e['date_spent']} | Category: {e['category']} | Amount: {e['amount']} | Desc: {e['description']}")

def calculate_total(expenses):
    if not expenses:
        print("No expense records yet.")
        return
    
    total = sum(e["amount"] for e in expenses)
    print(f"Total Expenses Amount: {total}")

def category_wise_spending(expenses):
    if not expenses:
        print("No expense records yet.")
        return

    totals = {}
    for e in expenses:
        category = e["category"]
        amount = e["amount"]
        totals[category] = totals.get(category, 0.0) + amount

    print("\n--- Category-Wise Spending ---")
    for category, amount in totals.items():
        print(f"{category}: {amount}")

def save_expenses(expenses):
    try:
        with open("expensesRecords.json", "w") as json_file:
            json.dump(expenses, json_file, indent=4)
        print("Expenses saved successfully!")
    except PermissionError:
        print("Permission denied: Cannot write to file.")

def load_expenses():
    try:
        with open("expensesRecords.json", "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        # Return an empty list if file doesn't exist yet so app doesn't crash
        return []
    except json.JSONDecodeError:
        print("Error reading save file. Starting with empty list.")
        return []