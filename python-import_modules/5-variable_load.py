#!/usr/bin/python3
import variable_load_5


def main():
    for x in variable_load_5:
        if dir(variable_load_5[x]) == "a": 
            print("{}".format(variable_load_5[x]))


if __name__ == "__main__":
    main()
