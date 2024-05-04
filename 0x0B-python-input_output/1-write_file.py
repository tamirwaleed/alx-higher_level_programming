#!/usr/bin/python3
""" function that writes """


def write_file(filename="", text=""):
    """ the parameters are filename and text """
    with open(filename, "w"):
        return fd.write(text)
