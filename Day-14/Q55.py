# Write a program to Second largest element.

arr = [10, 20, 50, 40, 30]

largest = arr[0]

for i in range(len(arr)):
    if arr[i] > largest:
        largest = arr[i]

second = arr[0]

for i in range(len(arr)):
    if arr[i] > second and arr[i] < largest:
        second = arr[i]

print("Second largest element is:", second)