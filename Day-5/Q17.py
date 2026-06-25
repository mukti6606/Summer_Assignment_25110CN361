# Write a program to Check perfect number.

num = int(input("Enter a number: "))

sum = 0    #Sum of divisors

for i in range(1, num):
    if num % i == 0:
        sum = sum + i

if sum == num:
    print(num, "is a Perfect Number")
else:
    print(num, "is not a Perfect Number")