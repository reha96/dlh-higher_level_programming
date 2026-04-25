#!/usr/bin/python3
def uppercase(str):
    input = str
    for i in range(len(input)):
        x = ord(input[i])
        if x >= 97 and x <= 123:
            x -= 32
        print("{}".format(chr(x)), end="")
    print("")
