# Write a program to Check string rotation

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

if len(str1) != len(str2):
    print("Not a rotation")
else:
    temp = str1 + str1

    if str2 in temp:
        print("Rotation")
    else:
        print("Not a rotation")