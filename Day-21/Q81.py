# Write a program to Find string length without strlen()

s = input("Enter a string: ")     

count = 0

for ch in s:
    count = count + 1

print("Length of string =", count)