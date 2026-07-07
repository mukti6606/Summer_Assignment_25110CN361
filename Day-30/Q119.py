# Write a program to Create mini employee management system

emp_id = []
emp_name = []
emp_salary = []

while True:
    print("\n----- Employee Management System -----")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        eid = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = input("Enter Employee Salary: ")

        emp_id.append(eid)
        emp_name.append(name)
        emp_salary.append(salary)

        print("Employee added successfully.")

    elif choice == 2:
        if len(emp_id) == 0:
            print("No employee records found.")
        else:
            print("\nEmployee Records")
            print("ID\tName\tSalary")

            for i in range(len(emp_id)):
                print(emp_id[i], "\t", emp_name[i], "\t", emp_salary[i])

    elif choice == 3:
        search = input("Enter Employee ID to Search: ")

        found = False

        for i in range(len(emp_id)):
            if emp_id[i] == search:
                print("\nEmployee Found")
                print("Employee ID:", emp_id[i])
                print("Name:", emp_name[i])
                print("Salary:", emp_salary[i])
                found = True
                break

        if found == False:
            print("Employee not found.")

    elif choice == 4:
        delete = input("Enter Employee ID to Delete: ")

        found = False

        for i in range(len(emp_id)):
            if emp_id[i] == delete:
                emp_id.pop(i)
                emp_name.pop(i)
                emp_salary.pop(i)
                print("Employee deleted successfully.")
                found = True
                break

        if found == False:
            print("Employee not found.")

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")