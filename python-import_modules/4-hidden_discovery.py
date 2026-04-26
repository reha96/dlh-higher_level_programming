#!/usr/bin/python3
import sys


def main(*argv):
    for i in range(len(argv)):
        if argv[i][0] != "_" and argv[i][1] != "_": 
            print(f"{argv[i]}")


if __name__ == "__main__":
    main(*sys.argv[1:])
