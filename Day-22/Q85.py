# Write a program to Check palindrome string

string = input("Enter a string: ")

reverse = ""

for ch in string:
    reverse = ch + reverse

if string == reverse:
    print("Palindrome String")
else:
    print("Not a Palindrome String")