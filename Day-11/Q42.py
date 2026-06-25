# Write a program to Write function to find maximum.

def max(a, b):           #For finding the maximum number
    if a > b:
        return a
    else:
        return b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = max(num1, num2)

print("Maximum number =", result)