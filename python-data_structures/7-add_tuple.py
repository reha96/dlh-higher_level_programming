#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = list(tuple_a)
    y = list(tuple_b)
    for i in range(2):
        if len(tuple_a) < 2 or len(tuple_b) < 2:
            x.append(0)
            y.append(0)
    tuple_a = tuple(x)
    tuple_b = tuple(y)
    sum_1 = tuple_a[0] + tuple_b[0]
    sum_2 = tuple_a[1] + tuple_b[1]
    sum = sum_1, sum_2
    return sum
