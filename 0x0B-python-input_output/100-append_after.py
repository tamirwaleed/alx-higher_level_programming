#!/usr/bin/python3
""" Advanced modules """


def append_after(filename="", search_string="", new_string=""):
    """ the function """
    with open(filename, "r+") as fd:
        lnlt = []
        while True:
            fileread = fd.readline()
            if fileread = "":
                break
            lnlt.append(fileread)
            if search_string in fileread:
                lnlt.append(new_string)
        fd.writelines(lnlt)
