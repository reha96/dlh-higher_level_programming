#!/usr/bin/python3
def print_last_digit(number):
    # string = str(number)[-1]
    # digit = int(string)
    # print("{}".format(digit), end="")
    print("{}".format(number % 10), end="")
    