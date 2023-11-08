#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        test = my_list[0]
        for i in range(len(my_list)):
            if test < my_list[i]:
                test = my_list[i]
        return (test)
    else:
        return (None)

