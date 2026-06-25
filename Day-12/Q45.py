# Write a program to Write function for palindrome.

def palindrome(text):
    reverse_text = ""

    for ch in text:
        reverse_text = ch + reverse_text

    if text == reverse_text:
        return True
    else:
        return False

word = input("Enter a word: ")

if palindrome(word):
    print("Palindrome")
else:
    print("Not a Palindrome")
