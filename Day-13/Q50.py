# Write a program to Find sum and average of array.

n = int(input("Enter number of elements: "))

arr = [0] * n

for i in range(n):
    arr[i] = int(input("Enter element: "))

sum = 0

for i in range(n):
    sum = sum + arr[i]

average = sum / n

print("Sum =", sum)
print("Average =", average)