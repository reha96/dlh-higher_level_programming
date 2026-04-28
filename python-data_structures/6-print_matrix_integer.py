#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if i>0:
            print(f"\n", end="")
        for j in range(len(matrix[i])):
            print("{:d} ".format(matrix[i][j]), end="")
    print(f"\n", end="")
