#!/usr/bin/python3

"""tester file"""

"""tester T1"""
Rectangle = __import__('0-rectangle').Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

"""tester T2"""    
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)

try:
    my_rectangle.width = -2
    my_rectangle.height = -1
    print(my_rectangle.__dict__)
except (IndexError, TypeError, ValueError) as err:
    print(err)

try:
    my_rectangle.width = 12
    my_rectangle.height = -2
    print(my_rectangle.__dict__)
except (IndexError, TypeError, ValueError) as err:
    print(err)