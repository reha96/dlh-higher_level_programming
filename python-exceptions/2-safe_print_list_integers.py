#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    skipped = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
            except:
                print(i)
                skipped += 1
    except:
        pass
    finally:
        print("")
        return i-skipped+1
