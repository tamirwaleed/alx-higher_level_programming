#!/usr/bin/python3
''' Module '''


class MyList(list):
    ''' Child of list '''
    def print_sorted(self):
        ''' prints a sorted list '''
        x = sorted(self)
        print(x)
