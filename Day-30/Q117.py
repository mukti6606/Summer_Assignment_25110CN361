# Write a program to Create student record system using arrays and strings

roll = []
name = []
course = []

while True:
    print("\n----- Student Record System -----")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        r = input("Enter Roll Number: ")
        n = input("Enter Student Name: ")
        c = input("Enter Course: ")

        roll.append(r)
        name.append(n)
        course.append(c)

        print("Student record added successfully.")

    elif choice == 2:
        if len(roll) == 0:
            print("No student records found.")
        else:
            print("\nStudent Records")
            print("Roll\tName\tCourse")

            for i in range(len(roll)):
                print(roll[i], "\t", name[i], "\t", course[i])

    elif choice == 3:
        search = input("Enter Roll Number to Search: ")

        found = False

        for i in range(len(roll)):
            if roll[i] == search:
                print("\nStudent Found")
                print("Roll Number:", roll[i])
                print("Name:", name[i])
                print("Course:", course[i])
                found = True
                break

        if found == False:
            print("Student not found.")

    elif choice == 4:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice")