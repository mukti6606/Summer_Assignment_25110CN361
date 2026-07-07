# Write a program to Find maximum occurring character

s = input("Enter a string: ")

max_count = 0
max_char = ""

for ch in s:
    count = s.count(ch)

    if count > max_count:
        max_count = count
        max_char = ch

print("Maximum occurring character is:", max_char)
print("It occurs", max_count, "times")