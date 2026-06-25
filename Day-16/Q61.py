# Write a program to Find missing number in array

arr = [1, 2, 3, 4, 6, 7]

count = 0
actual_sum = 0

# Find number of elements and their sum
for num in arr:
    count = count + 1
    actual_sum = actual_sum + num

n = count + 1

# Find expected sum from 1 to n
expected_sum = 0
for i in range(1, n + 1):
    expected_sum = expected_sum + i

missing_number = expected_sum - actual_sum

print("Missing number is:", missing_number)