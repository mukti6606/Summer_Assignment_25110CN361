# Write a program to Find longest word

sentence = input("Enter a sentence: ")

word = ""
longest = ""

for ch in sentence:
    if ch != " ":
        word = word + ch
    else:
        if len(word) > len(longest):
            longest = word
        word = ""

if len(word) > len(longest):
    longest = word

print("Longest word:", longest)
print("Length:", len(longest))