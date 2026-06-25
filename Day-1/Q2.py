# Write a program to Print multiplication table of a given number.

num = int(input("Enter a number: "))

print("\nMultiplication Table of", num, "is:")

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

