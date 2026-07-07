# Write a program to Create library management system

books = []

while True:
    print("\n----- Library Management System -----")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Remove Book")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added successfully.")

    elif choice == "2":
        if len(books) == 0:
            print("No books in the library.")
        else:
            print("\nAvailable Books:")
            for i in range(len(books)):
                print(i + 1, ".", books[i])

    elif choice == "3":
        search = input("Enter book name to search: ")

        if search in books:
            print("Book found.")
        else:
            print("Book not found.")

    elif choice == "4":
        remove = input("Enter book name to remove: ")

        if remove in books:
            books.remove(remove)
            print("Book removed successfully.")
        else:
            print("Book not found.")

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")