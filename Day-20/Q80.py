# Write a program to Find row-wise sum

r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))

a = []

print("Enter matrix elements:")
for i in range(r):
    row = []
    for j in range(c):
        row = row + [int(input())]
    a = a + [row]

for j in range(c):
    s = 0
    for i in range(r):
        s = s + a[i][j]
    print("Sum of column", j + 1, "=", s)