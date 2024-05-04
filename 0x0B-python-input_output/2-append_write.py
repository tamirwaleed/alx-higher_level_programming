#!/usr/bin/python3
""" function that appends """


def append_write(filename="", text=""):
    """ the parameters are filename and text """
    with open(filename, "a") as fd:
        return fd.write(text)
