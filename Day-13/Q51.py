# Write a program to Find largest and smallest element.

n = int(input("Enter number of elements: "))

arr = [0] * n

for i in range(n):
    arr[i] = int(input("Enter element: "))

largest = arr[0]
smallest = arr[0]

for i in range(n):
    if arr[i] > largest:
        largest = arr[i]

    if arr[i] < smallest:
        smallest = arr[i]

print("Largest element =", largest)
print("Smallest element =", smallest)