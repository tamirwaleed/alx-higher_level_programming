#!/usr/bin/python3
""" module for text identation """


def text_indentation(text):
    """ the function """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for x in ":?.":
        text = (x + "\n\n").join(
            [line.strip(" ") for line in text.split(x)])
    print(text, end="")
