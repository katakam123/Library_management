FILE_NAME = "expenses.txt"
def add_expense():
    print("\n--- Add Expense ---")

    date = input("Enter date (DD-MM-YYYY): ").strip()
    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()

    if date == "" or category == "" or description == "":
        print("Error: All fields are required.")
        return

    try:
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Error: Amount must be greater than 0.")
            return

    except ValueError:
        print("Error: Please enter a valid amount.")
        return

    with open(FILE_NAME, "a") as file:
        file.write(f"{date}|{category}|{description}|{amount}\n")

    print("Expense added successfully!")
def view_expenses():
    print("\n--- All Expenses ---")

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No expenses found.")
            return

        print("-" * 75)
        print(f"{'No.':<5}{'Date':<15}{'Category':<15}"
              f"{'Description':<25}{'Amount':>10}")
        print("-" * 75)

        for i, line in enumerate(lines, start=1):
            data = line.strip().split("|")

            if len(data) == 4:
                date, category, description, amount = data

                print(f"{i:<5}{date:<15}{category:<15}"
                      f"{description:<25}₹{float(amount):>9.2f}")

        print("-" * 75)

    except FileNotFoundError:
        print("No expense file found. Add an expense first.")
def total_expenses():
    print("\n--- Total Expenses ---")

    total = 0

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 4:
                    total += float(data[3])

        print(f"Total Expenses: ₹{total:.2f}")

    except FileNotFoundError:
        print("No expenses found.")

def search_by_category():
    print("\n--- Search by Category ---")

    category_search = input("Enter category: ").strip().lower()

    if category_search == "":
        print("Error: Category cannot be empty.")
        return

    found = False

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split("|")

                if len(data) == 4:
                    date, category, description, amount = data

                    if category.lower() == category_search:
                        print(
                            f"Date: {date} | "
                            f"Category: {category} | "
                            f"Description: {description} | "
                            f"Amount: ₹{float(amount):.2f}"
                        )
                        found = True

        if not found:
            print("No expenses found for this category.")

    except FileNotFoundError:
        print("No expenses found.")


# Delete an expense
def delete_expense():
    print("\n--- Delete Expense ---")

    try:
        with open(FILE_NAME, "r") as file:
            lines = file.readlines()

        if not lines:
            print("No expenses available.")
            return

        view_expenses()

        try:
            choice = int(input("Enter expense number to delete: "))

            if choice < 1 or choice > len(lines):
                print("Error: Invalid expense number.")
                return

        except ValueError:
            print("Error: Please enter a valid number.")
            return

        deleted_expense = lines.pop(choice - 1)

        with open(FILE_NAME, "w") as file:
            file.writelines(lines)

        print("Expense deleted successfully!")
        print("Deleted:", deleted_expense.strip())

    except FileNotFoundError:
        print("No expenses found.")

# Main menu
def main():
    while True:
        print("\n==============================")
        print("      MINI EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Search by Category")
        print("4. Calculate Total Expenses")
        print("5. Delete Expense")
        print("6. Exit")
        print("==============================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            search_by_category()

        elif choice == "4":
            total_expenses()

        elif choice == "5":
            delete_expense()

        elif choice == "6":
            print("Thank you for using Mini Expense Tracker!")
            break

        else:
            print("Error: Invalid choice. Please try again.")


# Start program
if __name__ == "__main__":
    main()