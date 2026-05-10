#!/usr/bin/python3
"""
Create a function def pascal_triangle(n): that returns a list of lists
of integers representing the Pascal's triangle of n:

    Returns an empty list if n <= 0
    You can assume n will be always an integer
    You are not allowed to import any module

"""


def pascal_triangle(n):
    """
    Create the n-triangle
    """
    if n <= 0:
        return []
    a = [[0] * n for _ in range(n)]

    for i in range(n):
        a[i][0] = 1
        a[i][i] = 1
        for j in range(1, n):
            a[i][j] = int(a[i - 1][j - 1]) + int(a[i - 1][j])
    for i in range(n):
        a[i] = a[i][: i + 1]

    return a
