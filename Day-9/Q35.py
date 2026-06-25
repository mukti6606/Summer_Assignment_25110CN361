# Write a program to Print repeated character pattern.
# A
# BB
# CCC
# DDDD
# EEEEE

for i in range(1, 6):
    ch = chr(64 + i)        # A, B, C, D, E

    for j in range(i):
        print(ch, end="")

    print()