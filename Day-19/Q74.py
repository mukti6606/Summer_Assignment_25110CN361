# Write a program to Subtract matrices

r = int(input("Enter number of rows: "))            #r stands for rows
c = int(input("Enter number of columns: "))         #c stands for columns

a = [[0 for j in range(c)] for i in range(r)]
b = [[0 for j in range(c)] for i in range(r)]

print("Enter elements of first matrix:")
for i in range(r):
    for j in range(c):
        a[i][j] = int(input())

print("Enter elements of second matrix:")
for i in range(r):
    for j in range(c):
        b[i][j] = int(input())

print("Difference of matrices:")

for i in range(r):
    for j in range(c):
        print(a[i][j] - b[i][j], end=" ")
    print()