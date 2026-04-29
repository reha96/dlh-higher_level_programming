#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    out = {}
    for i in a_dictionary:
        out[i] = a_dictionary[i]*2
    return out
