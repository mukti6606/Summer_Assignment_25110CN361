# Write a program to Find diagonal sum

n = int(input("Enter size of matrix: "))

a = [[0 for j in range(n)] for i in range(n)]

print("Enter matrix elements: ")
for i in range(n):
    for j in range(n):
        a[i][j] = int(input())

s = 0

for i in range(n):
    s = s + a[i][i]

print("Diagonal Sum =", s)