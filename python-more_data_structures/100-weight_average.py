#!/usr/bin/python3
def weight_average(my_list=[]):
    out_1 = 0
    out_2 = 0
    for i in my_list:
        out_1 += i[0] * i[1]
        out_2 += i[1]
    return out_1/out_2
