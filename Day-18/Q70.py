# Write a program to Selection sort

arr = [64, 25, 12, 22, 11]

for i in range(5):
    min = i

    for j in range(i + 1, 5):
        if arr[j] < arr[min]:
            min = j

    temp = arr[i]
    arr[i] = arr[min]
    arr[min] = temp

print("Sorted array:")
for i in range(5):
    print(arr[i], end=" ")