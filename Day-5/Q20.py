# Write a program to Find largest prime factor

num = int(input("Enter a number: "))

largest_prime = 1

for i in range(2, num + 1):
    if num % i == 0:
        is_prime = True

        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break

        if is_prime:
            largest_prime = i

print("Largest Prime Factor =", largest_prime)