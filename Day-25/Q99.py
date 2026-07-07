# Write a program to Sort names alphabetically

n = int(input("Enter the number of names: "))

names = []

for i in range(n):
    name = input("Enter a name: ")
    names.append(name)

# Bubble Sort
for i in range(n):
    for j in range(n - 1):
        if names[j] > names[j + 1]:
            temp = names[j]
            names[j] = names[j + 1]
            names[j + 1] = temp

print("Names in alphabetical order:")
for i in names:
    print(i)