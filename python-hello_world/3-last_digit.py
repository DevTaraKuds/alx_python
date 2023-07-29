#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# # YOUR CODE HERE
# number=str(number)
# lastDigit = abs(int(number[-1]))

# if lastDigit > 5:
#     valueText = "and is greater than 5"
# elif (lastDigit < 6) and (lastDigit != 0):
#     valueText = "and is less than 6 and not 0"
# else:
#     valueText = "and is 0"


# print("Last digit of", number, "is", lastDigit, valueText, end="\n")

# Get the last digit of the number
last_digit = number % 10

# Check the last digit and print the output accordingly
if last_digit > 5:
    print("Last digit of", number, "is", last_digit, "and is greater than 5")
elif last_digit == 0:
    print("Last digit of", number, "is", last_digit, "and is 0")
else:
    print("Last digit of", number, "is", -last_digit, "and is less than 6 and not 0")

