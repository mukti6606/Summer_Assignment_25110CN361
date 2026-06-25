# Write a program to Find factorial of a number.

n = int(input("Enter a number whose factorial you want: "))

if(n <= 0):
    print("Please enter a natural number")
elif(n == 1):
    print("The factorial is 1")
else:
    product = 1
    for i in range(2, n+1):
        product = product * i
        i = i + 1
    print("The factorial of the given number is", product)
