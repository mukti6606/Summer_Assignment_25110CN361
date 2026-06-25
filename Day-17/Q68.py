# Write a program to Find common elements

# Input first array
n1 = int(input("Enter size of first array: "))
arr1 = []

for i in range(n1):
    arr1 = arr1 + [int(input())]

# Input second array
n2 = int(input("Enter size of second array: "))
arr2 = []

for i in range(n2):
    arr2 = arr2 + [int(input())]

# Find common elements
print("Common elements are:")

for i in arr1:
    for j in arr2:
        if i == j:
            print(i, end=" ")
            break