# Write a program to Reverse a string

s = input("Enter a string: ")

rev = ""

for ch in s:
    rev = ch + rev

print("Reversed string =", rev)