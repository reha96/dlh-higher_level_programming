#!/usr/bin/python3
def roman_to_int(roman_string):
    out = 0
    if type(roman_string) is not str or type(roman_string) is None:
        return None
    for i in range(len(roman_string)):
        if roman_string[i] == "M" and roman_string[i-1] == "C":
            out += 900
        elif roman_string[i] == "M":
            out += 1000
        if roman_string[i] == "D" and roman_string[i-1] == "C":
            out += 400
        elif roman_string[i] == "D":
            out += 500
        elif roman_string[i] == "C":
            out += 100
        if roman_string[i] == "L" and roman_string[i-1] == "X":
            out += 40
        elif roman_string[i] == "L":
            out += 50
        if roman_string[i] == "X":
            if roman_string[i-1] == "I" and i != 0:
                out += 9
            else:
                out += 10
        if (roman_string[i] == "V" and (i == 0)) or (roman_string[i] == "V" and roman_string[i-1] != "I"):
            out += 5
        elif roman_string[i] == "V" and roman_string[i-1] == "I":
            out += 4
    for i in range(len(roman_string)):
        if i > 0:
            if (roman_string[-i] == "I" and roman_string[-i-1] != "X") or roman_string[-i] == "I" and roman_string[-i-1] != "V":
                out += 1
    return out
