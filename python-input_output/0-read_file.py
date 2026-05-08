#!/usr/bin/python3
"""This module writes a function that reads a
text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    try:
        with open(filename, "r") as file:
            print(file.read())
    except Exception as err:
        print(err)