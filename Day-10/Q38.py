# Write a program to Print reverse pyramid.
#    *********
#     *******
#      *****
#       ***
#        *

rows = 5

for i in range(rows, 0, -1):
    spaces = rows - i
    stars = 2 * i - 1

    print(" " * spaces + "*" * stars)