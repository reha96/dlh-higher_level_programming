#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
string = str(number)[-1]
digit = int(string)
if number < 0 and type(number)==int:
    digit = -digit
if digit > 5: 
    print(f"Last digit of {number} is {digit} and is greater than 5")
elif digit == 0:
    print(f"Last digit of {number} is {digit} and is 0")
else:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
    