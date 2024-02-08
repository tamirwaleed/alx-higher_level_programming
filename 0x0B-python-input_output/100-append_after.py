#!/usr/bin/python3
""" Advanced modules """


def append_after(filename="", search_string="", new_string=""):
    """ the function """
    with open(filename, "r+") as fd:
        i = 0
        fileread = fd.readlines()
        for line in fileread:
            if line.find(search_string) is not -1:
                fileread.insert(i + 1, new_string)
            i += 1
        fd.seek(0)
        fd.write("".join(fileread))
    return fd
