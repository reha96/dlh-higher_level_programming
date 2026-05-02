#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    skipped = 0

    for i in range(x):
        try:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
        except TypeError:
            skipped += 1
    print("")
    return i-skipped+1