#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    out = []
    for i in range(len(matrix)):
        out.append(list(map(lambda x: x*x, matrix[i])))
    return out
