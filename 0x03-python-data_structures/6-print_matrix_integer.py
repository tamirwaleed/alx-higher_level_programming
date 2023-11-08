#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for hnai in matrix: 
        for i in hnai:
            print("{:d}".format(i), end=" " if i != hnai[-1] else "")
        print()
