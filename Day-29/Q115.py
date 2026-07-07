# Write a program to Create menu-driven string operations system

while True:
    print("\n----- MENU -----")
    print("1. Find Length")
    print("2. Convert to Uppercase")
    print("3. Convert to Lowercase")
    print("4. Reverse String")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Program Closed.")
        break

    s = input("Enter a string: ")

    if choice == 1:
        print("Length =", len(s))

    elif choice == 2:
        print("Uppercase =", s.upper())

    elif choice == 3:
        print("Lowercase =", s.lower())

    elif choice == 4:
        print("Reversed String =", s[::-1])

    else:
        print("Invalid Choice!")