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
    a = [[0] * n] * n
    sum = [0] * n

    a[0] = [1] + a[0]
    for i in range(len(a[0])):
        sum[0] += a[0][i]

    a[1] = [1] + a[0]
    for i in range(len(a[1])):
        sum[1] += a[1][i]

    a[2] = [1] + a[1]
    a[2][1] += 1
    a[3] = [1] + a[2]
    # a[2][1] += 1

    try:
        print(f"out: {a} \n sum: {sum} ")
    except:
        pass

    # for n in range(1, n+1):
    # size = [1 for n in range(1, n+1)]
    # out.append(size)
    # sum.append(0)

    # for i in range(len(out)):
    #     out[i][0] = 1
    #     out[i][-1] = 1
    #     for j in range(len(out[i])):
    #         if out[i][j] == 0:
    #             out[i][j] = sum[i]
    #         sum[i] += out[i][j]

    # for i in range(n):
    #     out[i][0] = 1
    #     out[i][-1] = 1
    #     for j in range(len(out[i])):
    #         sum[i] += out[i][j]
    #     if i > 1:
    #         out[i][i // 2] = sum[i]
    #     for j in range(len(out[i])):
    #         sum[i] += out[i][j]

    # sum[i] += out[i][i]
    # if n > 2:
    # print(n // 2)
    # for n in range(n):
    #     out[i][j].append(1)

    # # for n in range(n):
    # while out[n] == 0:
    #     out[n] = out[n - 1] + out[n + 1]


# def print_triangle(triangle):
#     """
#     Print the triangle
#     """
#     for row in triangle:
#         print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    # print_triangle(pascal_triangle(5))
    # pascal_triangle(0)
    # pascal_triangle(1)
    # pascal_triangle(2)
    # pascal_triangle(3)
    # pascal_triangle(4)
    pascal_triangle(5)
