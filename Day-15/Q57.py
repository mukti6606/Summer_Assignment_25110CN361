# Write a program to Reverse array

n = int(input("Enter number of elements: "))

a = [0] * n

for i in range(n):
    a[i] = int(input("Enter element: "))

print("Reversed Array:")

for i in range(n - 1, -1, -1):
    print(a[i], end=" ")