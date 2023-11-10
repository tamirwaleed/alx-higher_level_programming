#!/usr/bin/python3
def best_score(a_dictionary):
    maxo = 0
    who = ""
    if a_dictionary:
        for x in a_dictionary:
            if a_dictionary[x] > maxo:
                maxo, who = a_dictionary[x], x
        return (who)
    else:
        return None
