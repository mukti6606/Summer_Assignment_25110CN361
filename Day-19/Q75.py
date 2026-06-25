# Write a program to Transpose matrix

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

a = [[0 for j in range(c)] for i in range(r)]

print("Enter matrix elements: ")
for i in range(r):
    for j in range(c):
        a[i][j] = int(input())

print("Transpose of matrix: ")

for j in range(c):
    for i in range(r):
        print(a[i][j], end=" ")
    print()