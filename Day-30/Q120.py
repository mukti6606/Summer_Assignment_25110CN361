# Write a program to Develop complete mini project using arrays, strings and functions

            # "Student Management System" as a Mini Project

roll = []
name = []
course = []

        
# Function to add student
def add_student():
    r = input("Enter Roll Number: ")
    n = input("Enter Name: ")
    c = input("Enter Course: ")

    roll.append(r)
    name.append(n)
    course.append(c)

    print("Student Added Successfully.")

        
# Function to display students
def display_student():
    if len(roll) == 0:
        print("No Student Records Found.")
    else:
        print("\nRoll\tName\tCourse")
        for i in range(len(roll)):
            print(roll[i], "\t", name[i], "\t", course[i])

        
# Function to search student
def search_student():
    s = input("Enter Roll Number to Search: ")

    found = False

    for i in range(len(roll)):
        if roll[i] == s:
            print("\nStudent Found")
            print("Roll Number :", roll[i])
            print("Name :", name[i])
            print("Course :", course[i])
            found = True
            break

    if found == False:
        print("Student Not Found.")

# Function to delete student
def delete_student():
    d = input("Enter Roll Number to Delete: ")

    found = False

    for i in range(len(roll)):
        if roll[i] == d:
            roll.pop(i)
            name.pop(i)
            course.pop(i)
            print("Student Deleted Successfully.")
            found = True
            break

    if found == False:
        print("Student Not Found.")

# Main Program
while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_student()

    elif choice == 3:
        search_student()

    elif choice == 4:
        delete_student()

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")