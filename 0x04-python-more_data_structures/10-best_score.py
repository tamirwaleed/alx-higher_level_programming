#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        return(map(lambda x, y: x if a_dictioary[x] > a_dictionary[y] else y, a_dictionary))
    else: 
        return None
