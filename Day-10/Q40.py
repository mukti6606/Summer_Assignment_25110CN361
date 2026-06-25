# Write a program to Print character pyramid.
#         A
#        ABA
#       ABCBA
#      ABCDCBA
#     ABCDEDCBA

rows = 5

for i in range(1, rows + 1):
    print(" " * (rows - i), end="")

    # Increasing characters
    for j in range(i):
        print(chr(65 + j), end="")

    # Decreasing characters
    for j in range(i - 2, -1, -1):
        print(chr(65 + j), end="")

    print()