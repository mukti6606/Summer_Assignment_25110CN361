# Write a program to Frequency of an element. 

arr = [10, 20, 30, 20, 40, 20, 50]

num = int(input("Enter element to find frequency: "))

count = 0

for i in range(len(arr)):
    if arr[i] == num:
        count = count + 1

print("Frequency of", num, "is", count)
