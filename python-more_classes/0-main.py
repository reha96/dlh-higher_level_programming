#!/usr/bin/python3
"""tester file"""
import os


class More_Classes:

    task = 0

    def __init__(self):
        print()
        
    def welcome(self, value=0):
        if isinstance(value, int) and value >= 0 and value <= 9:
            self.task = value
        else:
            raise TypeError(
                "insert the task number you want to test as an integer! first task is 0, last is 9")
            

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
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
          my_rectangle.perimeter()))

    print("--")

    my_rectangle.width = 0
    my_rectangle.height = 3
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
          my_rectangle.perimeter()))

    """tester T4"""
    print("--")
    print("tester T4")
    print("--")

    Rectangle = __import__("3-rectangle").Rectangle

    my_rectangle = Rectangle(2, 4)
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
          my_rectangle.perimeter()))

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
    print("Area: {} - Perimeter: {}".format(my_rectangle.area(),
          my_rectangle.perimeter()))

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

    """tester T8"""
    os.system('clear')
    print("--"*10)
    print("tester T8")
    print("--"*10)
    os.system("pycodestyle 7-rectangle.py")
    print("--"*10)

    Rectangle = __import__('7-rectangle').Rectangle

    my_rectangle_1 = Rectangle(8, 4)
    print(my_rectangle_1)
    print("--")
    my_rectangle_1.print_symbol = "&"
    print(my_rectangle_1)
    print("--")

    my_rectangle_2 = Rectangle(2, 1)
    print(my_rectangle_2)
    print("--")
    Rectangle.print_symbol = "C"
    print(my_rectangle_2)
    print("--")

    my_rectangle_3 = Rectangle(7, 3)
    print(my_rectangle_3)

    print("--")

    try:
        my_rectangle_3.print_symbol = ["C", "is", "fun!"]
        print(my_rectangle_3)
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))

    print("--")

    """tester T9"""
    os.system('clear')
    print("--"*10)
    print("tester T9")
    print("--"*5 + "pycode" + "--"*5)
    os.system("pycodestyle 8-rectangle.py")
    print("--"*5 + "pycode" + "--"*5)

    Rectangle = __import__('8-rectangle').Rectangle

    my_rectangle_1 = Rectangle(8, 4)
    my_rectangle_2 = Rectangle(2, 3)

    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")

    my_rectangle_2.width = 10
    my_rectangle_2.height = 5
    if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
        print("my_rectangle_1 is bigger or equal to my_rectangle_2")
    else:
        print("my_rectangle_2 is bigger than my_rectangle_1")

    """tester T10"""
    os.system('clear')
    print("--"*10)
    print("tester T10")
    print("--"*5 + "pycode" + "--"*5)
    os.system("pycodestyle 9-rectangle.py")
    print("--"*5 + "pycode" + "--"*5)

    Rectangle = __import__('9-rectangle').Rectangle

    my_square = Rectangle.square(5)
    print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
    print(my_square)
