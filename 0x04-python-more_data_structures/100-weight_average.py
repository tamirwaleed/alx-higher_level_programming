#!/usr/bin/python3
def weight_average(my_list=[]):
    nume, den = 0, 0
    if my_list:
        for x, y in my_list:
            nume += x * y 
            den += y
        return (avg = nume / den)
    else:
        return 0
