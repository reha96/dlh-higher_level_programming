#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    out = list(map(lambda i: list(map(lambda x: x**2, i)), matrix))
    return out
