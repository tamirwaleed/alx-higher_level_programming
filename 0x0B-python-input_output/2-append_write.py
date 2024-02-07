#!/usr/bin/python3
""" Third module """


def append_write(filename="", text=""):
    """ appends to file """
    with open(filename, "a") as fd:
        return fd.write(text)
