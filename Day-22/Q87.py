# Write a program to Character frequency

string = input("Enter a string: ")
ch = input("Enter a character: ")

count = 0

for i in string:
    if i == ch:
        count = count + 1

print("Frequency of", ch, "=", count)