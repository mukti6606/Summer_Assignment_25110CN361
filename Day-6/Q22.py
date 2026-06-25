# Write a program to Convert binary to decimal

binary = int(input("Enter a binary number: "))

decimal = 0
base = 1

while binary > 0:
    digit = binary % 10
    decimal = decimal + digit * base
    base = base * 2
    binary = binary // 10

print("Decimal number is:", decimal)