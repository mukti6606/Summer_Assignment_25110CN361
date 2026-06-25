# Write a program to Check whether a number is palindrome.

n = int(input("Enter a number: "))

num = n
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if num == reverse:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")