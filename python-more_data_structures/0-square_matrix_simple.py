#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    out = []
    f = lambda x: x*x
    for i in range(len(matrix)):
        out.append(list(map(f, matrix[i])))
    return out
