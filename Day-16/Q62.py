# Write a program to Find maximum frequency element

arr = [1, 2, 2, 3, 4, 2, 3]

max_freq = 0
max_element = arr[0]

for i in range(len(arr)):
    count = 0

    for j in range(len(arr)):
        if arr[i] == arr[j]:
            count = count + 1

    if count > max_freq:
        max_freq = count
        max_element = arr[i]

print("Element with maximum frequency:", max_element)
print("Frequency:", max_freq)