import random

y = int(input("Enter a number from 1-10: "))
x = random.randint(1, 10)

if y == x:
    print("You got the correct number")
else:
    print("Please try again.")