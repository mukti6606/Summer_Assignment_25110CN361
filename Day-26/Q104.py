# Write a program to Create quiz application

score = 0

print("Welcome to the Quiz!")

print("\nQuestion 1: What is the capital of India?")
print("a. Mumbai")
print("b. Delhi")
print("c. Kolkata")
print("d. Chennai")
answer = input("Enter your answer (a/b/c/d): ")

if answer == "b":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print("\nQuestion 2: How many days are there in a week?")
print("a. 5")
print("b. 6")
print("c. 7")
print("d. 8")
answer = input("Enter your answer (a/b/c/d): ")

if answer == "c":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print("\nQuestion 3: What is the value of 35*5?")
print("a. 150")
print("b. 165")
print("c. 170")
print("d. 175")
answer = input("Enter your answer (a/b/c/d): ")

if answer == "a":
    print("Correct!")
    score = score + 1
else:
    print("Wrong!")

print("\nYour Final Score is:", score, "/3")