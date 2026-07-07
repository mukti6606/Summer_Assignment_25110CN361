# Write a program to Create mini library system

book = []
author = []

while True:
    print("\n----- Mini Library System -----")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        b = input("Enter Book Name: ")
        a = input("Enter Author Name: ")

        book.append(b)
        author.append(a)

        print("Book added successfully.")

    elif choice == 2:
        if len(book) == 0:
            print("No books available.")
        else:
            print("\nBook List")
            print("Book Name\tAuthor")

            for i in range(len(book)):
                print(book[i], "\t", author[i])

    elif choice == 3:
        search = input("Enter Book Name to Search: ")

        found = False

        for i in range(len(book)):
            if book[i].lower() == search.lower():
                print("\nBook Found")
                print("Book Name:", book[i])
                print("Author:", author[i])
                found = True
                break

        if found == False:
            print("Book not found.")

    elif choice == 4:
        issue = input("Enter Book Name to Issue: ")

        found = False

        for i in range(len(book)):
            if book[i].lower() == issue.lower():
                print("Book Issued Successfully.")
                book.pop(i)
                author.pop(i)
                found = True
                break

        if found == False:
            print("Book not available.")

    elif choice == 5:
        print("Thank you for using the Library System.")
        break

    else:
        print("Invalid Choice.")