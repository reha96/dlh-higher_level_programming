#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if i>0:
            print(f"\n", end="")
        for j in range(len(matrix[i])):
            print("{:d}".format(matrix[i][j]), end="")
            if j != len(matrix[i])-1:
                print(" ", end="")
    print(f"\n", end="")
