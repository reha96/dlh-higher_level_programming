#!/usr/bin/python3
def roman_to_int(roman_string):
    out = 0
    if (type(roman_string) is not str) or (type(roman_string) is None):
        return out
    map = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    i = 0
    j = 0
    excep = False
    if len(roman_string) == 1:
        out += map[roman_string[i]]
        return out
    # 1 length case, no comparison
    for i in range(len(roman_string)):
        if excep is True:
            excep = False
            continue
        for j in range(len(roman_string)):
            if i == len(roman_string) - 1:
                out += map[roman_string[i]]  # standard case
                return out
            if i == j or i > j or j - i > 1:
                continue
            if (map[roman_string[i]] >= map[roman_string[j]]):
                out += map[roman_string[i]]  # standard case
            elif map[roman_string[i]] < map[roman_string[j]]:
                if roman_string[i] == "I" and roman_string[j] == "X":
                    out += 9  # exception IX
                    excep = True
                if roman_string[i] == "I" and roman_string[j] == "V":
                    out += 4  # exception IV
                    excep = True
                if roman_string[i] == "X" and roman_string[j] == "L":
                    out += 40  # exception XL
                    excep = True
                if roman_string[i] == "X" and roman_string[j] == "C":
                    out += 90  # exception XC
                    excep = True
                if roman_string[i] == "C" and roman_string[j] == "D":
                    out += 400  # exception CD
                    excep = True
    return out
