#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
number=str(number)
lastDigit = int(number[-1])

if lastDigit > 5:
    valueText = "and is greater than 5"
elif (lastDigit < 6) and (lastDigit != 0):
    valueText = "and is less than 6 and not 0"
else:
    valueText = "and is 0"


print("Last digit of", number, "is", lastDigit, valueText, end="\n" )
