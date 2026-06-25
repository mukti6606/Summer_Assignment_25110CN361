# Write a program to Print prime numbers in a range.

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Prime numbers in the given range are:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num)