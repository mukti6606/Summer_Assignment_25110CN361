# Write a program to Create menu-driven array operations system

arr = []

while True:
    print("\n----- MENU -----")
    print("1. Add Element")
    print("2. Display Array")
    print("3. Search Element")
    print("4. Delete Element")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter element to add: "))
        arr.append(num)
        print("Element Added.")

    elif choice == 2:
        print("Array:", arr)

    elif choice == 3:
        num = int(input("Enter element to search: "))
        if num in arr:
            print("Element Found.")
        else:
            print("Element Not Found.")

    elif choice == 4:
        num = int(input("Enter element to delete: "))
        if num in arr:
            arr.remove(num)
            print("Element Deleted.")
        else:
            print("Element Not Found.")

    elif choice == 5:
        print("Program Closed.")
        break

    else:
        print("Invalid Choice!")