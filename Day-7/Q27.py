# Write a program to Recursive sum of digits

def sum(n):           #Here, sum means "sum of digits"
    if n == 0:
        return 0
    else:
        return (n % 10) + sum(n // 10)

num = int(input("Enter a number: "))

print("Sum of digits =", sum(num))