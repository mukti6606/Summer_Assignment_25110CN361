# Write a program to Find common characters in strings

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

print("Common characters are:")

for i in str1:
    if i in str2:
        print(i, end=" ")