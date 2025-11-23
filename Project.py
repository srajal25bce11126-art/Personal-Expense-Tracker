expense = {}
def add_expense():
    category = input("Enter category: ")
    date = input("Enter date (DD-MM-YYYY): ")
    description = input("Enter description: ")
    amount = int(input("Enter amount: "))
    expense[category] = {"Date" : date,
                        "Description" : description,
                        "Amount" : amount
                        }
    print("Expense added successfully!\n")

def view_expenses():
    category = input("Enter the category name: ")
    if category not in expense:
        return

    Exp = expense[category]
    print(f"----Expense of {category}------")
    print("date of expense: ",Exp["Date"])    
    print("Reason of Expense: ",Exp["Description"])    
    print("Money used: ",Exp["Amount"])

def total_expenses():
    total = 0
    for i in expense:
        exp = expense[i]["Amount"]
        total += exp
        print("Total Expenses: ₹", total, "\n")

def categor_sum():
    for cat, amt in expense.items():
            print(cat, " : ", amt)

def Expense_tracker():
    while True:
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Expenses")
        print("4. Category wise summary")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            categor_sum()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.\n")

Expense_tracker()
