# Write a program to Remove duplicates from array

arr = [1, 2, 2, 3, 4, 3, 5]

n = 0
for x in arr:
    n = n + 1

for i in range(n):
    duplicate = False

    for j in range(i):
        if arr[i] == arr[j]:
            duplicate = True
            break

    if duplicate == False:
        print(arr[i], end=" ")