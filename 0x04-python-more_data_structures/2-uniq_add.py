#!/usr/bin/python3
def uniq_add(my_list=[]):
    newl = set(my_list)
    from functools import reduce
    return (reduce(lambda x, y: x + y, newl))
