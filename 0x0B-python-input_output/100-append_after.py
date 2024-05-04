#!/usr/bin/python3
""" append at the end of each line """


def append_after(filename="", search_string="", new_string=""):
    """ takes the parameters filename and strings """
    with open(filename, "r") as fd:
        total = ""
        lines = fd.readlines()
        for line in lines:
            if line.find(search_string) != -1:
                text = line + new_string
            else:
                text = line
            total = total + text
    with open(filename, "w") as fd:
        fd.write(total)
