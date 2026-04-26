#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv 


def main(*argv):
    if len(argv) != 2:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    a = int(argv[0])
    b = int(argv[2])
    operator = argv[1]
    if operator == "+":
        print("{} ".format(a) + "{} ".format(operator) + "{} = ".format(b) + "{}".format(add(a, b)))
    elif operator == "-":
        print("{} ".format(a) + "{} ".format(operator) + "{} = ".format(b) + "{}".format(sub(a, b)))
    elif operator == "*":
        print("{} ".format(a) + "{} ".format(operator) + "{} = ".format(b) + "{}".format(mul(a, b)))
    elif operator == "/":
        print("{} ".format(a) + "{} ".format(operator) + "{} = ".format(b) + "{}".format(div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")


if __name__ == "__main__":
    main(*argv[1:])
