# Write a program to Find the first repeating character

s = input("Enter a string: ")

        # Finding the first repeating character
for i in range(len(s)):
    count = 0

    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1

    if count > 1:
        print("First repeating character is:", s[i])
        break
else:
    print("No repeating character found")