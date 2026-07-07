# Write a program to Create bank account system

balance = 0

while True:
    print("\n----- Bank Account System -----")
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Amount deposited successfully.")

    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))

        if amount <= balance:
            balance = balance - amount
            print("Amount withdrawn successfully.")
        else:
            print("Insufficient balance.")

    elif choice == "3":
        print("Current Balance =", balance)

    elif choice == "4":
        print("Thank you for using the Bank Account System.")
        break

    else:
        print("Invalid choice.")