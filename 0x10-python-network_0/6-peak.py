#!/usr/bin/python3
''' function that finds a peak in a list of unsorted integers '''


def find_peak(list_of_integers):
    ''' the function which takes the list '''
    if (len(list_of_integers) > 0):
        return max(list_of_integers)
    else:
        return None
