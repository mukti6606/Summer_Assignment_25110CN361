# Write a program to Create contact management system

names = []
numbers = []

while True:
    print("\n----- Contact Management System -----")
    print("1. Add Contact")
    print("2. Display Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Name: ")
        number = input("Enter Phone Number: ")

        names.append(name)
        numbers.append(number)

        print("Contact added successfully.")

    elif choice == "2":
        if len(names) == 0:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for i in range(len(names)):
                print(names[i], "-", numbers[i])

    elif choice == "3":
        search = input("Enter name to search: ")

        if search in names:
            index = names.index(search)
            print("Name:", names[index])
            print("Phone Number:", numbers[index])
        else:
            print("Contact not found.")

    elif choice == "4":
        delete = input("Enter name to delete: ")

        if delete in names:
            index = names.index(delete)
            names.pop(index)
            numbers.pop(index)
            print("Contact deleted successfully.")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")