#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    out_1 = 0
    try:
        for x in range(x):
            print(my_list[x], end="")
            out_1 = x+1
    except:
            return out_1
    finally:
        print("")
        return out_1
