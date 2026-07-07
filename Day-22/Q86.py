# Write a program to Count words in a sentence.

sentence = input("Enter a sentence: ")

count = 1

for ch in sentence:
    if ch == " ":
        count = count + 1

print("Number of words =", count)
