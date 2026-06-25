# Write a program to Sort array in descending order

arr = [10, 30, 20, 50, 40]

for i in range(5):
    for j in range(i + 1, 5):
        if arr[i] < arr[j]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print("Array in descending order:")

for i in range(5):
    print(arr[i], end=" ")