#!/usr/bin/python3
""" Second module """


def write_file(filename="", text=""):
    """ write file """
    with open(filename, "w") as fd:
        fd.write(text)
        for i,text in enumerate(text):
            pass
        return i
