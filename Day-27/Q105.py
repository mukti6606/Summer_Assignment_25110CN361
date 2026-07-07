# Write a program to Create student record management system

students = []

while True:
    print("\n----- Student Record Management System -----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = input("Enter Roll Number: ")
        name = input("Enter Name: ")
        marks = input("Enter Marks: ")

        students.append([roll, name, marks])
        print("Student record added successfully.")

    elif choice == 2:
        if len(students) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records:")
            print("Roll No\tName\tMarks")
            for i in students:
                print(i[0], "\t", i[1], "\t", i[2])

    elif choice == 3:
        roll = input("Enter Roll Number to search: ")
        found = False

        for i in students:
            if i[0] == roll:
                print("Record Found")
                print("Roll Number:", i[0])
                print("Name:", i[1])
                print("Marks:", i[2])
                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice == 4:
        roll = input("Enter Roll Number to delete: ")
        found = False

        for i in students:
            if i[0] == roll:
                students.remove(i)
                print("Record deleted successfully.")
                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice == 5:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")