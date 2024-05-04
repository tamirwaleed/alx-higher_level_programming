#!/usr/bin/python3
""" Function that reads text files """


def read_file(filename=""):
    """ the function that takes filename """
    with open(filename, "r") as fd:
        print(fd.read(), end="")
