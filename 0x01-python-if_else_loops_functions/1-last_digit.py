#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)

last_digit = number % 10 if number >= 0 else -((-number) % 10)

output_string = "Last digit of {} is {} and is".format(number, last_digit)

if last_digit < 5:
    print(output_string + " greater than 5")
elif last_digit == 0:
    print(output_string + " 0")
else:
    print(output_string + " less than 6 and not 0")
