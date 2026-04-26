#!/usr/bin/python3
import sys


def main(*argv):
    if len(argv) == 0:
        print("0 arguments.")
    elif len(argv) == 1:
        print("1 argument:")
        print(f"{len(argv)}: {argv[0]}")     
    else:
        print(f"{len(argv)} arguments:")
        for i in range(len(argv)):
            print(f"{i+1}: {argv[i]}")

if __name__ == "__main__":
    main(*sys.argv[1:])
