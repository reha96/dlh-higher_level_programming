#!/usr/bin/python3


def main(argv = None):
    if argv == None:
        print("0 arguments.")
    elif len(argv) == 1:
        print("1 argument:")
        print(f"{len(argv)}: {argv}")     
    else:
        print(f"{len(argv)} arguments:")
        for i in range(len(argv)):
            print(f"{i}: {argv[i]}")

if __name__ == "__main__":
    main()
