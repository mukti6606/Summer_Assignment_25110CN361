# Write a program to Create marksheet generation system

print("----- Marksheet Generation System -----")

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

m1 = int(input("Enter marks of Subject 1: "))
m2 = int(input("Enter marks of Subject 2: "))
m3 = int(input("Enter marks of Subject 3: "))
m4 = int(input("Enter marks of Subject 4: "))
m5 = int(input("Enter marks of Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 40:
    grade = "D"
else:
    grade = "Fail"

print("\n----- Marksheet -----")
print("Student Name :", name)
print("Roll Number  :", roll)
print("Subject 1    :", m1)
print("Subject 2    :", m2)
print("Subject 3    :", m3)
print("Subject 4    :", m4)
print("Subject 5    :", m5)
print("Total Marks  :", total)
print("Percentage   :", percentage)
print("Grade        :", grade)