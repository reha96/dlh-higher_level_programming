#!/usr/bin/python3
from calculator_1 import add, sub, mul, div


def main(a, operator, b):
    if a is None or operator is None or b is None:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    a = int(a)
    b = int(b)
    if operator == "+":
        print("{}".format(a) + "{}".format(operator) + "{} = ".format(b) + "{}".format(add(a, b)))
    elif operator == "-":
        print("{}".format(a) + "{}".format(operator) + "{} = ".format(b) + "{}".format(sub(a, b)))
    elif operator == "*":
        print("{}".format(a) + "{}".format(operator) + "{} = ".format(b) + "{}".format(mul(a, b)))
    elif operator == "/":
        print("{}".format(a) + "{}".format(operator) + "{} = ".format(b) + "{}".format(div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")


if __name__ == "__main__":
    main()
