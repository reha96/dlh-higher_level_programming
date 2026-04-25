#!/usr/bin/python3
for i in range(98):
    if i < 97:
        print("{:02d}".format(i)+", ", end="")
    else:
        print("{}".format(i))
