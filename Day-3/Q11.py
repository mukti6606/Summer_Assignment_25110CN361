# Write a program to Find GCD of two numbers.

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

gcd = 1

for i in range(1, min(x, y) + 1):
    if x % i == 0 and y % i == 0:
        gcd = i

print("GCD of", x, "and", y, "is", gcd)