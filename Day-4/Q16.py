# Write a program to Print Armstrong numbers in a range.

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

print("Armstrong numbers in the given range are:")

for num in range(start, end + 1):
    original = num
    digits = len(str(num))
    total = 0

    temp = num
    while temp > 0:
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10

    if total == original:
        print(original)
