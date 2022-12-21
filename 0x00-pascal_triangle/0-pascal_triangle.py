#!/usr/bin/python3
'''A module for working with Pascal's triangle.
'''


def pascal_triangle(n):
    '''Creates a list of lists of integers representing
    the Pascal's triangle of a given integer.
    '''
    triangle = []
    if type(n) is not int or n <= 0:
                return triangle
    for row in range(n):
        if row == 0:
            triangle.append([1])
        else:
            triangle.append([1] + [triangle[row-1][i] + triangle[row-1][i+1] for i in range(row-1)] + [1])
    return triangle
