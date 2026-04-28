#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    out = []
    for i in my_list:
        if i % 2 == 0:
            out.append(True)
        else:
            out.append(False)
    return out
