# Write a program to Recursive reverse number

def rev_num(n, rev):        #Here, rev_num means "reverse number"
    if n == 0:
        return rev
    else:
        return rev_num(n // 10, rev * 10 + n % 10)

num = int(input("Enter a number: "))

print("Reversed number =", rev_num(num, 0))