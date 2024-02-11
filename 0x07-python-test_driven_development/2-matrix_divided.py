#!/usr/bin/python3
""" defines the divide module """


def matrix_divided(matrix, div):
    """ the function """
    if ((type(matrix) is not list) or matrix == []
            or not all(type(row) is list for row in matrix)
            or not all(type(ele) in (int, float)
                       for ele in [num for row in matrix for num in row])):
        raise TypeError("matrix must be a matrix (list of lists) of "
                "integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    result = []
    for row in matrix:
        temp = []
        for elem in row:
            temp.append(round((elem / div), 2))
        result.append(temp)
    return result
