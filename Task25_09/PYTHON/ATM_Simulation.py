balance = 20000.00
# Check balance
def check_balance():
    print("\n--- Balance Inquiry ---")
    print(f"Available Balance: ₹{balance:.2f}")
# Deposit money
def deposit():
    global balance

    print("\n--- Deposit Money ---")

    try:
        amount = float(input("Enter deposit amount: ₹"))

        if amount <= 0:
            print("Error: Deposit amount must be greater than 0.")
            return

        balance += amount

        print(f"₹{amount:.2f} deposited successfully.")
        print(f"Updated Balance: ₹{balance:.2f}")

    except ValueError:
        print("Error: Please enter a valid amount.")
# Withdraw money
def withdraw():
    global balance

    print("\n--- Withdraw Money ---")

    try:
        amount = float(input("Enter withdrawal amount: ₹"))

        if amount <= 0:
            print("Error: Withdrawal amount must be greater than 0.")
            return

        if amount > balance:
            print("Error: Insufficient balance.")
            return

        balance -= amount

        print(f"₹{amount:.2f} withdrawn successfully.")
        print(f"Remaining Balance: ₹{balance:.2f}")

    except ValueError:
        print("Error: Please enter a valid amount.")
# Main ATM menu
def atm_menu():
    while True:
        print("\n==============================")
        print("       ATM SIMULATION")
        print("==============================")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        print("==============================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            check_balance()

        elif choice == "2":
            deposit()

        elif choice == "3":
            withdraw()

        elif choice == "4":
            print("\nThank you for using the ATM.")
            print("Please collect your card.")
            break

        else:
            print("Error: Invalid choice. Please select 1-4.")
1
# Start the program
if __name__ == "__main__":
    atm_menu()