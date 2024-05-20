#!/usr/bin/python3
""" module for printing a square """


def print_square(size):
    """ printing a square """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    sq = ""
    for i in range(size):
        for j in range(size):
            sq += "#"
        sq += "\n"
    print(sq[:-1])
