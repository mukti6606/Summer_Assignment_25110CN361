# Write a program to Write function for Armstrong.

def armstrong(num):
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total = total + (digit ** 3)
        temp = temp // 10

    if total == num:
        return True
    else:
        return False


num = int(input("Enter a number: "))

if armstrong(num):
    print("The given number is a Armstrong Number")
else:
    print("The given number is a Not an Armstrong Number")