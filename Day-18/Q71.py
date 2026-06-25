# Write a program to Binary search

arr = [10, 20, 30, 40, 50]

x = int(input("Enter number: "))

first = 0
last = 4

while first <= last:

    mid = (first + last) // 2

    if arr[mid] == x:
        print("Found")
        break

    if x < arr[mid]:
        last = mid - 1
    else:
        first = mid + 1

if first > last:
    print("Not Found")