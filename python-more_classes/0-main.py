#!/usr/bin/python3

"""tester file"""

"""tester T1"""
print("--")
print("tester T1")
print("--")
Rectangle = __import__("0-rectangle").Rectangle

my_rectangle = Rectangle()
print(type(my_rectangle))
print(my_rectangle.__dict__)

"""tester T2"""
print("--")
print("tester T2")
print("--")
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
print("--")
print("tester T3")
print("--")
Rectangle = __import__("2-rectangle").Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print("--")

my_rectangle.width = 0
my_rectangle.height = 3
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

"""tester T4"""
print("--")
print("tester T4")
print("--")

Rectangle = __import__("3-rectangle").Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

print(str(my_rectangle))
print(repr(my_rectangle))

print("--")

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle)
print(repr(my_rectangle))

try:
    my_rectangle.width = 0
    my_rectangle.height = 0
    print(my_rectangle)
    print(repr(my_rectangle))
except Exception as err:
    print("[{}] {}".format(err.__class__.__name__, err))

try:
    my_rectangle.width = -9
    my_rectangle.height = 0
    print(my_rectangle)
    print(repr(my_rectangle))
except Exception as err:
    print("[{}] {}".format(err.__class__.__name__, err))

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))

"""tester T5"""
print("--")
print("tester T5")
print("--")

Rectangle = __import__("4-rectangle").Rectangle

my_rectangle = Rectangle(2, 4)
print(str(my_rectangle))
print("--")
print(my_rectangle)
print("--")
print(repr(my_rectangle))
print("--")
print(hex(id(my_rectangle)))
print("--")

# create new instance based on representation
new_rectangle = eval(repr(my_rectangle))
print(str(new_rectangle))
print("--")
print(new_rectangle)
print("--")
print(repr(new_rectangle))
print("--")
print(hex(id(new_rectangle)))
print("--")

print(new_rectangle is my_rectangle)
print(type(new_rectangle) is type(my_rectangle))

"""tester T6"""
print("--")
print("tester T6")
print("--")

Rectangle = __import__("5-rectangle").Rectangle

my_rectangle = Rectangle(2, 4)
print("Area: {} - Perimeter: {}".format(my_rectangle.area(), my_rectangle.perimeter()))

del my_rectangle

try:
    print(my_rectangle)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))

"""tester T7"""
print("--")
print("tester T7")
print("--")

Rectangle = __import__("6-rectangle").Rectangle

my_rectangle_1 = Rectangle(2, 4)
my_rectangle_2 = Rectangle(2, 4)
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_1
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
del my_rectangle_2
print("{:d} instances of Rectangle".format(Rectangle.number_of_instances))
