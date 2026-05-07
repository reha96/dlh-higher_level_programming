#!/usr/bin/python3

"""tester file"""

"""tester T1"""
Rectangle = __import__("0-rectangle").Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

"""tester T2"""
Rectangle = __import__("1-rectangle").Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

try:
    my_rectangle = Rectangle(-2, -4)
    print(my_rectangle.__dict__)
except Exception as err:
    print("[{}] {}".format(err.__class__.__name__, err))

try:
    my_rectangle.width = 2
    my_rectangle.height = -3
    print(my_rectangle.__dict__)
except Exception as err:
    print("[{}] {}".format(err.__class__.__name__, err))

"""tester T3"""
