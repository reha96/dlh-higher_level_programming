#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    out = 0
    try:
        for x in range(x):
            print(my_list[x], end="")
            out += 1
    except (IndexError):
        pass
    finally:
        print("")
        return out
