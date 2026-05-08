#!/usr/bin/python3
"""This module writes a function that writes a
string to a text file (UTF8) and returns the nb
of chars"""


def write_file(filename="", text=""):
    """a function that writes a
    string to a text file (UTF8) and returns the nb
    of chars"""
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(text)
        with open(filename, "r", encoding="utf-8") as file:
            return len(file.read())
    except Exception as err:
        print("[{}] {}".format(err.__class__.__name__, err))
