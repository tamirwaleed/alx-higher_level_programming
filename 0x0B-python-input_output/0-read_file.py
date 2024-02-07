#!/usr/bin/python3
""" First Module """


def read_file(filename=""):
    """ the function """
    with open(filename, "r") as fd:
        rdfile = fd.read()
    print(rdfile, end = "")
