#!/usr/bin/python3
"""This module writes a function that reads a
text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """a function that reads a
    text file (UTF8) and prints it to stdout"""

    try:
        with open(filename, "r") as file:
            print(file.read(), end="")
    except Exception as err:
        print("[{}] {}".format(err.__class__.__name__, err))
