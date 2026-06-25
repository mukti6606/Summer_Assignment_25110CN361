# Write a program to Multiply matrices

            # Input rows and columns
r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))

r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))

            # Check if multiplication is possible
if c1 != r2:
    print("Matrix multiplication is not possible")
else:
    A = []                      # First matrix
    print("Enter elements of first matrix:")
    for i in range(r1):
        row = []
        for j in range(c1):
            row = row + [int(input())]
        A = A + [row]

    B = []                      # Second matrix
    print("Enter elements of second matrix:")
    for i in range(r2):
        row = []
        for j in range(c2):
            row = row + [int(input())]
        B = B + [row]

    result = []                 # Result matrix
    for i in range(r1):
        row = []
        for j in range(c2):
            row = row + [0]
        result = result + [row]

            # Matrix multiplication
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] = result[i][j] + A[i][k] * B[k][j]

            # Display result
    print("Resultant Matrix:")
    for i in range(r1):
        for j in range(c2):
            print(result[i][j], end=" ")
        print()