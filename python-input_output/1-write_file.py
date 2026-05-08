#!/usr/bin/python3
"""This module writes a function that writes a
string to a text file (UTF8) and prints it
to stdout"""


def write_file(filename="", text=""):
    try:
        with open(filename, "a") as file:
            file.write(text)
    except Exception as err:
        print("[{}] {}".format(err.__class__.__name__, err))
