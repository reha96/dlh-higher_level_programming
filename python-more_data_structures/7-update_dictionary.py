#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    insert = (key, value)
    a_dictionary.update([insert])
    return a_dictionary
