# Write a program to Check whether a number is prime.

x = int(input("Enter a number to check whether it is prime or not: "))

if(x < 0 or x == 0):
    print("Enter a positive number")
elif(x==1):
    print("1 is not a prime number")
else:
    for i in range(2, x):
        if (x % i == 0):
            print("Given number is not a prime number")
            break
    else:
        print("Given number is a prime number")

