# Write a program to Sort words by length

n = int(input("Enter the number of words: "))

words = [0] * n

        # Input words
for i in range(n):
    words[i] = input("Enter a word: ")

        # Solving it using Bubble Sort based on length
for i in range(n):
    for j in range(n - 1):
        if len(words[j]) > len(words[j + 1]):
            temp = words[j]
            words[j] = words[j + 1]
            words[j + 1] = temp

print("Words sorted by length:")

for i in range(n):
    print(words[i])