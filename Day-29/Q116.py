# Write a program to Create inventory management system

items = []
quantity = []

while True:
    print("\n----- INVENTORY MANAGEMENT SYSTEM -----")
    print("1. Add Item")
    print("2. Display Inventory")
    print("3. Search Item")
    print("4. Delete Item")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter item name: ")
        qty = int(input("Enter quantity: "))

        items.append(name)
        quantity.append(qty)

        print("Item Added Successfully.")

    elif choice == 2:
        if len(items) == 0:
            print("Inventory is Empty.")
        else:
            print("\nItems\t\tQuantity")
            for i in range(len(items)):
                print(items[i], "\t\t", quantity[i])

    elif choice == 3:
        name = input("Enter item name to search: ")

        if name in items:
            index = items.index(name)
            print("Item Found")
            print("Quantity =", quantity[index])
        else:
            print("Item Not Found.")

    elif choice == 4:
        name = input("Enter item name to delete: ")

        if name in items:
            index = items.index(name)
            items.pop(index)
            quantity.pop(index)
            print("Item Deleted.")
        else:
            print("Item Not Found.")

    elif choice == 5:
        print("Program Closed.")
        break

    else:
        print("Invalid Choice!")