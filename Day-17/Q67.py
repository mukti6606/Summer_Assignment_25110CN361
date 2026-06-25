# Write a program to Intersection of arrays

#Input first array
n1 = int(input("Enter size of first array: "))
arr1 = []

for i in range(n1):
    arr1 = arr1 + [int(input())]

#Input second array
n2 = int(input("Enter size of second array: "))
arr2 = []

for i in range(n2):
    arr2 = arr2 + [int(input())]

# Find intersection
intersection = []

for i in arr1:
    for j in arr2:
        if i == j:
            intersection = intersection + [i]
            break

# Display result
print("Intersection of arrays:")
for i in intersection:
    print(i, end=" ")