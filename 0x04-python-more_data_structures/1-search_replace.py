#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newl = my_list[:]
    for i in range(len(my_list)):
        if my_list[i] == search:
            newl[i] = replace
        else:
            newl[i] = my_list[i]
    return (newl)
