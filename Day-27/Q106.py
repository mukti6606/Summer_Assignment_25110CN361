# Write a program to Create employee management system

employees = []

while True:
    print("\n----- Employee Management System -----")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = input("Enter Salary: ")

        employees.append([emp_id, name, salary])
        print("Employee record added successfully.")

    elif choice == 2:
        if len(employees) == 0:
            print("No employee records found.")
        else:
            print("\nEmployee Records:")
            print("ID\tName\tSalary")
            for i in employees:
                print(i[0], "\t", i[1], "\t", i[2])

    elif choice == 3:
        emp_id = input("Enter Employee ID to search: ")
        found = False

        for i in employees:
            if i[0] == emp_id:
                print("\nEmployee Found")
                print("Employee ID:", i[0])
                print("Name:", i[1])
                print("Salary:", i[2])
                found = True
                break

        if found == False:
            print("Employee not found.")

    elif choice == 4:
        emp_id = input("Enter Employee ID to delete: ")
        found = False

        for i in employees:
            if i[0] == emp_id:
                employees.remove(i)
                print("Employee record deleted successfully.")
                found = True
                break

        if found == False:
            print("Employee not found.")

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")