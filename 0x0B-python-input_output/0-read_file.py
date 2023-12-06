#!/usr/bin/python3
''' Module for reading files '''


def read_file(filename=""):
    ''' Function '''
    with open(filename) as fd:
        print(fd.read(), end="")
