# Personal Expense Tracker

expenses = []

def add_expense():
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    print("Expense added successfully!\n")


def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return

    print("\nAll Expenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['category']} - {exp['amount']}")
    print()


def total_spent():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\nTotal Spent: {total}\n")


def highest_expense():
    if not expenses:
        print("No expenses recorded.\n")
        return

    highest = max(expenses, key=lambda x: x["amount"])
    print(f"\nHighest Expense: {highest['category']} - {highest['amount']}\n")


def view_by_category():
    category = input("Enter category to filter: ")

    filtered = [exp for exp in expenses if exp["category"].lower() == category.lower()]

    if not filtered:
        print("No expenses found for this category.\n")
        return

    print(f"\nExpenses in {category}:")
    for exp in filtered:
        print(f"{exp['category']} - {exp['amount']}")
    print()


def menu():
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Total Spent")
        print("4. Highest Expense")
        print("5. View by Category")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_spent()
        elif choice == "4":
            highest_expense()
        elif choice == "5":
            view_by_category()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")


menu()