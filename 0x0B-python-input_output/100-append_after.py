#!/usr/bin/python3
""" Advanced modules """


def append_after(filename="", search_string="", new_string=""):
    """ the function """
    with open(filename, "r+") as fd:
        fileread = fd.readlines()
        i = 0
        for line in fileread:
            if search_string in line:
                fileread.insert(i + 1, new_string)
            i += 1
        fd.seek(0)
        fd.write("".join(fileread))
