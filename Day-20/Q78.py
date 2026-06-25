# Write a program to Check symmetric matrix

n = int(input("Enter order of matrix: "))

a = []

print("Enter matrix elements:")
for i in range(n):
    row = []
    for j in range(n):
        row = row + [int(input())]
    a = a + [row]

symmetric = True

for i in range(n):
    for j in range(n):
        if a[i][j] != a[j][i]:
            symmetric = False

if symmetric:
    print("Matrix is Symmetric")
else:
    print("Matrix is Not Symmetric")