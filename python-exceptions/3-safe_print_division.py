#!/usr/bin/python3
def safe_print_division(a, b):
    out = 0
    try:
        out = a/b
    except ZeroDivisionError:
        out = None
    finally:
        print("Inside result: ", end="")
        print("{}".format(out))
        return out
