# Write a program to Check Armstrong number.

num = int(input("Enter a number: "))

original = num
digits = len(str(num))
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit ** digits
    num = num // 10

if sum == original:
    print(original, "is an Armstrong number")
else:
    print(original, "is not an Armstrong number")