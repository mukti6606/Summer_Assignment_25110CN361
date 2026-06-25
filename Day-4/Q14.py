# Write a program to Find nth Fibonacci term.

n = int(input("Enter the value of n: "))

a = 0
b = 1

if n == 1:
    print("Nth Fibonacci term =", a)
elif n == 2:
    print("Nth Fibonacci term =", b)
else:
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c

    print("Nth Fibonacci term =", b)