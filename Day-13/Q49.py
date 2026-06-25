# Write a program to Input and display array. 

n = int(input("Enter number of elements: "))

arr = [0] * n

for i in range(n):
    arr[i] = int(input("Enter element: "))

print("Array elements are:")

for i in range(n):
    print(arr[i])