# Write a program to Union of arrays

# Input first array
n1 = int(input("Enter size of first array: "))
arr1 = []

for i in range(n1):
    arr1 = arr1 + [int(input())]

#Input second array
n2 = int(input("Enter size of second array: "))     
arr2 = []

for i in range(n2):
    arr2 = arr2 + [int(input())]

# Find union
union = arr1

for i in arr2:
    found = 0

    for j in union:
        if i == j:
            found = 1
            break

    if found == 0:
        union = union + [i]

# Display union array
print("Union of arrays:")
for i in union:
    print(i, end=" ")