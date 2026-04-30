#!/usr/bin/python3
def roman_to_int(roman_string):
    out = 0
    if type(roman_string) is not str or type(roman_string) is None:
        return None
    map = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    i = 0
    j = 0
    excep = False
    if len(roman_string) == 1:
        out += map[roman_string[i]]
    # 1 length case, no comparison
    for i in range(len(roman_string)):
        if excep == True:
            excep = False
            continue
        for j in range(len(roman_string)):
            if i == j or i > j or j - i > 1 or excep:
                continue
            if map[roman_string[i]] >= map[roman_string[j]] or i == len(roman_string):
                out += map[roman_string[i]]  # standard case
                print(f"{map[roman_string[i]]} add std")
            elif map[roman_string[i]] < map[roman_string[j]]:
                if roman_string[i] == "I" and roman_string[j] == "X":
                    out += 9  # exception IX
                    excep = True
                    print(f"IX")
                if roman_string[i] == "I" and roman_string[j] == "V":
                    out += 4  # exception IV
                    excep = True
                    print(f"IV")
                if roman_string[i] == "X" and roman_string[j] == "L":
                    out += 40  # exception XL
                    excep = True
                    print(f"XL")
                if roman_string[i] == "X" and roman_string[j] == "C":
                    out += 90  # exception XC
                    excep = True
                    print(f"XC")
                if roman_string[i] == "C" and roman_string[j] == "D":
                    out += 400  # exception CD
                    excep = True
                    print(f"CD")
    return out
