#!/usr/bin/python3
""" Advanced modules """


def append_after(filename="", search_string="", new_string=""):
    """ the function """
    with open(filename, "r+") as fd:
        lnlt = []
        while True:
            line = fd.readline()
            if line == "":
                break
            lnlt.append(line)
            if search_string in line:
                lnlt.append(new_string)
        fd.writelines(lnlt)
