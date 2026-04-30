#!/usr/bin/python3
def roman_to_int(roman_string):
    out = 0
    if type(roman_string) is not str or type(roman_string) is None:
        return None
    for i in range(len(roman_string)):
        if roman_string[i] == "M" and roman_string[i-1] == "C":
            print("add 900")
            out += 900
        elif roman_string[i] == "M":
            print("add 1000")
            out += 1000
        if roman_string[i] == "D" and roman_string[i-1] == "C":
            print("add 400")
            out += 400
        elif roman_string[i] == "D":
            print("add 500")
            out += 500
        elif roman_string[i] == "C":
            print("add 100")
            out += 100
        if roman_string[i] == "L" and roman_string[i-1] == "X":
            print("add 40")
            out += 40
        elif roman_string[i] == "L":
            print("add 50")
            out += 50
        if roman_string[i] == "X":
            if roman_string[i-1] == "I" and i != 0:
                print("add 9")
                out += 9
            else:
                print("add 10")
                out += 10
        if (roman_string[i] == "V" and (i == 0)) or (roman_string[i] == "V" and roman_string[i-1] != "I"):
            print("add 5")
            out += 5
        elif roman_string[i] == "V" and roman_string[i-1] == "I":
            print("add 4")
            out += 4
    for i in range(len(roman_string)):
        if i > 0:
            if (roman_string[-i] == "I" and roman_string[-i-1] != "X") or roman_string[-i] == "I" and roman_string[-i-1] != "V":
                print("add 1")
                out += 1
    return out
