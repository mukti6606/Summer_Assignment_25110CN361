# Write a program to Rotate array right

n = int(input("Enter number of elements: "))

a = [0] * n

for i in range(n):
    a[i] = int(input("Enter element: "))

temp = a[n - 1]

for i in range(n - 1, 0, -1):
    a[i] = a[i - 1]

a[0] = temp

print("Array after right rotation:")

for i in range(n):
    print(a[i], end=" ")