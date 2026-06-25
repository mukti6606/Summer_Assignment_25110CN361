# Write a program to Write function for perfect number

def perfect(num):
    total = 0

    for i in range(1, num):
        if num % i == 0:
            total = total + i

    if total == num:
        return True
    else:
        return False


num = int(input("Enter a number: "))

if perfect(num):
    print("The given number is a Perfect Number")
else:
    print("The given number is a Not a Perfect Number")