import datetime
from ex import Expense
import calendar

def main():
    expense_file_path = "expense.csv"
    try:
        budget = float(input("Enter the Budget for this month: "))
    except ValueError:
        print("Invalid input for budget. Please enter a numerical value.")
        return

    # Get the expense object
    expense = expense_amount_tillnow()

    # Save the expense to file
    save_me_file(expense, expense_file_path)

    # Summarize expenses
    summarize_expense(expense_file_path, budget)

def expense_amount_tillnow():
    print("How much money spent: ")
    expense_name = input("Where are you spending: ")
    try:
        expense_amount = float(input("How much money are you spending: "))
    except ValueError:
        print("Invalid amount. Please enter a numerical value.")
        return expense_amount_tillnow()  # Retry input

    print(f"Expense Name: {expense_name}, Amount: {expense_amount}")

    expense_category = [
        "Food",
        "Home",
        "Work",
        "Fun",
        "Misc"
    ]

    while True:
        print("Select the category of expense:")
        for i, category_name in enumerate(expense_category):
            print(f"{i + 1}. {category_name}")

        try:
            selected_index = int(input(f"Choose a category (1-{len(expense_category)}): ")) - 1
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the category.")
            continue

        if 0 <= selected_index < len(expense_category):
            selected_category = expense_category[selected_index]
            print(f"Selected Category: {selected_category}")

            new_expense = Expense(name=expense_name, category=selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid Category. Please try again.")

def save_me_file(expense: Expense, expense_file_path: str):
    print(f"Saving the expenditure: {expense} to {expense_file_path}")
    try:
        with open(expense_file_path, "a") as f:
            f.write(f"{expense.name},{expense.category},{expense.amount}\n")
        print("Expense saved successfully.")
    except Exception as e:
        print(f"An error occurred while saving the expense: {e}")

def summarize_expense(expense_file_path, budget):
    expenses = []
    print("\nSummarizing Expenses...\n")
    try:
        with open(expense_file_path, "r") as f:
            lines = f.readlines()
            for line in lines:
                # Correct the order: name, category, amount
                expense_name, expense_category, expense_amount = line.strip().split(",")
                print(f"Name: {expense_name}, Category: {expense_category}, Amount: {expense_amount}")
                try:
                    line_expense = Expense(name=expense_name, category=expense_category, amount=float(expense_amount))
                    expenses.append(line_expense)
                except ValueError:
                    print(f"Invalid amount for expense '{expense_name}'. Skipping.")
    except FileNotFoundError:
        print("No expenses recorded yet.")
        return
    except Exception as e:
        print(f"An error occurred while reading the expenses: {e}")
        return

    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    print("\nExpenses by Category:")
    for key, amount in amount_by_category.items():
        print(f"{key}: {amount:.2f}")

    total_spend = sum(x.amount for x in expenses)
    print(f"\nTotal Spending: {total_spend:.2f}")

    remaining_budget = budget - total_spend
    print(f"Remaining Budget: {remaining_budget:.2f}")

    # Calculate remaining days in the current month
    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    print(f"Days Remaining in the Month: {remaining_days}")

    if remaining_days > 0:
        daily_budget = remaining_budget / remaining_days
        print(f"Daily Budget: {daily_budget:.2f}")
    else:
        print("No days remaining in the month.")

if __name__ == "__main__":
    main()


