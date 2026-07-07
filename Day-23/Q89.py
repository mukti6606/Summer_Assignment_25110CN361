# Write a program to Find the first non-repeating character

s = input("Enter a string: ")

        # Finding the first non-repeating character
for ch in s:
    count = 0

    for c in s:
        if ch == c:
            count += 1

    if count == 1:
        print("First non-repeating character is:", ch)
        break
else:
    print("No non-repeating character found")