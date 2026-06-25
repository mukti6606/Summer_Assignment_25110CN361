# Write a program to Rotate array left.

n = int(input("Enter number of elements: "))

a = [0] * n

for i in range(n):
    a[i] = int(input("Enter element: "))

temp = a[0]

for i in range(n - 1):
    a[i] = a[i + 1]

a[n - 1] = temp

print("Array after left rotation:")

for i in range(n):
    print(a[i], end=" ")