#!/usr/bin/python3
"""A module that writes a function that
appends a string at the end of a text file (UTF8)
and returns the number of characters added
    """


def append_write(filename="", text=""):
    """a function that
    appends a string at the end of a text file
    (UTF8) and returns the number of characters
    added

    Args:
        filename (str, optional): _description_.
        Defaults to "".
        text (str, optional): _description_.
        Defaults to "".
    """
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text)
        return len(text)
