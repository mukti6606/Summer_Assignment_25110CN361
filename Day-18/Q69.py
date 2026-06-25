# Write a program to Bubble sort

arr = [5, 3, 8, 1, 2]

for i in arr:
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp

print("Sorted array:")
for i in arr:
    print(i, end=" ")