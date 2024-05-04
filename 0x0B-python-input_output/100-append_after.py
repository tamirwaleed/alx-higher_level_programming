#!/usr/bin/python3
""" append at the end of each line """


def append_after(filename="", search_string="", new_string=""):
    """ takes the parameters filename and strings """
    with open(filename, "r+") as fd:
        total = ""
        for line in fd.read():
            if search_string in line:
                text = line + new_string
            else:
                text = line
            total += text
        fd.write(total)

