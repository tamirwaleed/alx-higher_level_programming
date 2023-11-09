#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newl = []
    for x in matrix:
        newl.append(list(map(lambda x : x**2, x)))
    return (newl)
