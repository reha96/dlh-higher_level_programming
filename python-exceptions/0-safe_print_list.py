#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    out_1 = 0
    for x in range(x):
        try:
            print(my_list[x], end="")
            out_1 = x+1
        except:
            print("")
            return out_1
    print("")
    return out_1
