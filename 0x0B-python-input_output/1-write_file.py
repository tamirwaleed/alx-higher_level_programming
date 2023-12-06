#!/usr/bin/python3
''' Writing module '''


def write_file(filename="", text=""):
    ''' The function '''
    with open(filename, 'w') as fd:
        return (fd.write(text))
