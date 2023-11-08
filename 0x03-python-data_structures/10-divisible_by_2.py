#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        test = []
        for x in range(len(my_list)):
            if test[x] % 2 == 0:
                test[x] = True
            else:
                test[x] = False
    return (test)
