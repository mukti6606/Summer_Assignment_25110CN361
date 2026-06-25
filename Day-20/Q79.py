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

for i in range(r):
    s = 0
    for j in range(c):
        s = s + a[i][j]
    print("Sum of row", i + 1, "=", s)