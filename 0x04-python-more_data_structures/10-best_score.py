#!/usr/bin/python3
def best_score(a_dictionary):
    max = 0
    if a_dictionary:
        for x in a_dictionary:
            if a_dictionary[x] > max:
                max = a_dictionary[x]
        return (max)
    else: 
        return None
