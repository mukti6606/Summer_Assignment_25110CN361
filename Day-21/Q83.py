# Write a program to Count vowels and consonants

s = input("Enter a string: ")

vowels = 0
consonants = 0

for ch in s:
    if ch in "aeiouAEIOU":
        vowels = vowels + 1
    elif ch.isalpha():
        consonants = consonants + 1

print("Vowels =", vowels)
print("Consonants =", consonants)