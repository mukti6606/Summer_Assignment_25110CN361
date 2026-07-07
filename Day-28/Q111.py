# Write a program to Create ticket booking system

tickets = 10
price = 200

while True:
    print("\n----- Ticket Booking System -----")
    print("1. Book Ticket")
    print("2. Check Available Tickets")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        num = int(input("Enter number of tickets: "))

        if num <= tickets:
            total = num * price
            tickets = tickets - num

            print("Booking Successful!")
            print("Total Amount =", total)
            print("Tickets Left =", tickets)

        else:
            print("Sorry! Not enough tickets available.")

    elif choice == "2":
        print("Available Tickets =", tickets)

    elif choice == "3":
        print("Thank you for using the Ticket Booking System.")
        break

    else:
        print("Invalid choice.")