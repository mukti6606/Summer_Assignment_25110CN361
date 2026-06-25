# Write a program to Merge arrays

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

# Merge arrays
merged = arr1 + arr2

# Display merged array
print("Merged Array:")
for i in merged:
    print(i, end=" ")