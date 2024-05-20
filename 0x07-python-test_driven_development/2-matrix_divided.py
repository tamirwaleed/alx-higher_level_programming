#!/usr/bin/python3
""" the matrix_divided module """


def matrix_divided(matrix, div):
    """ the function that takes the matrix
    and the number (dividor) """
    if type(div) not in (int, float):
                raise TypeError("div must be a number")
    if div == 0:
                raise ZeroDivisionError("division by zero")
    new_mat = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        res = []
        for col in row:
            if type(col) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            res.append(round((col / div), 2))
        new_mat.append(res)
    return new_mat
