# Write a program to Create salary management system

salary_records = []

while True:
    print("\n----- Salary Management System -----")
    print("1. Add Salary Record")
    print("2. Display Salary Records")
    print("3. Search Salary Record")
    print("4. Delete Salary Record")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = input("Enter Salary: ")

        salary_records.append([emp_id, name, salary])
        print("Salary record added successfully.")

    elif choice == 2:
        if len(salary_records) == 0:
            print("No salary records found.")
        else:
            print("\nSalary Records:")
            print("ID\tName\tSalary")
            for i in salary_records:
                print(i[0], "\t", i[1], "\t", i[2])

    elif choice == 3:
        emp_id = input("Enter Employee ID to search: ")
        found = False

        for i in salary_records:
            if i[0] == emp_id:
                print("\nSalary Record Found")
                print("Employee ID:", i[0])
                print("Name:", i[1])
                print("Salary:", i[2])
                found = True
                break

        if found == False:
            print("Salary record not found.")

    elif choice == 4:
        emp_id = input("Enter Employee ID to delete: ")
        found = False

        for i in salary_records:
            if i[0] == emp_id:
                salary_records.remove(i)
                print("Salary record deleted successfully.")
                found = True
                break

        if found == False:
            print("Salary record not found.")

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")