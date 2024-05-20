#!/usr/bin/python3
""" module for printing a square """


def print_square(size):
    """ printing a square """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print((("#" * size + "\n") * size), end="")
    sq = ""
    for i in range(size):
        sq += "#" * size
        sq += "\n"
    print(sq[:-2])
