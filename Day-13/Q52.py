# Write a program to Count even and odd elements.

n = int(input("Enter number of elements: "))

arr = [0] * n

for i in range(n):
    arr[i] = int(input("Enter element: "))

even = 0
odd = 0

for i in range(n):
    if arr[i] % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even elements =", even)
print("Odd elements =", odd)