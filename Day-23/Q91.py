# Write a program to Check anagram strings

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("Strings are not anagrams")
else:
    flag = True

    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            flag = False
            break

    if flag:
        print("Strings are anagrams")
    else:
        print("Strings are not anagrams")