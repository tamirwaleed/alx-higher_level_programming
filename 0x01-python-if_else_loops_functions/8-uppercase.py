#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) in range(97, 123):
            c = chr(ord(str[i]) - 32)
            print(c, end="")
        else:
            print(str[i], end="")
    print("")
