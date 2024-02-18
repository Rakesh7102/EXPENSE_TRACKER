import json

class Expense:
    def __init__(self, date, category, amount):
        self.date = date
        self.category = category
        self.amount = amount
        

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    expense = Expense(date, category, amount)
    return expense

def view_expenses(expenses):
    for expense in expenses:
        print(f"Date: {expense.date}, Category: {expense.category}, Amount: {expense.amount}")

def save_expenses(expenses):
    with open("expenses.json", "w") as f:
        json.dump([vars(expense) for expense in expenses], f)

def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            data = json.load(f)
            expenses = [Expense(expense['date'], expense['category'], expense['amount']) for expense in data]
    except FileNotFoundError:
        expenses = []
    return expenses

def main():
    expenses = load_expenses()
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            expense = add_expense()
            expenses.append(expense)
            save_expenses(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
