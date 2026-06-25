# Write a program to Move zeroes to end

n = int(input("Enter number of elements: "))

a = [0] * n

for i in range(n):
    a[i] = int(input("Enter element: "))

for i in range(n):
    if a[i] == 0:
        for j in range(i, n - 1):
            a[j] = a[j + 1]
        a[n - 1] = 0

print("Array after moving zeroes to end:")

for i in range(n):
    print(a[i], end=" ")