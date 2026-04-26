#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv 


def main(*argv):
    if len(argv) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    a = int(argv[0])
    b = int(argv[2])
    operator = argv[1]
    if operator == "+":
        print(f"{a} {operator} {b} = {add(a, b)}")
    elif operator == "-":
        print(f"{a} {operator} {b} = {sub(a, b)}")
    elif operator == "*":
        print(f"{a} {operator} {b} = {mul(a, b)}")
    elif operator == "/":
        print(f"{a} {operator} {b} = {div(a, b)}")
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        raise ValueError()


if __name__ == "__main__":
    main(*argv[1:])
