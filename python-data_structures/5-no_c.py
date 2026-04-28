#!/usr/bin/python3
def no_c(my_string):
    for i in range(len(my_string)):
        if "C" in my_string:
            my_string = my_string.split('C')
            my_string = ' '.join(my_string)
        if "c" in my_string:
            my_string = my_string.split('c')
            my_string = ' '.join(my_string)
    return my_string
