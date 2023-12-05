#!/usr/bin/python3
''' REBELLION '''


class MyInt(int):
    ''' rebel child '''
    def __eq__(self, value):
        ''' to equate '''
        return self.real != value

    def __ne__(self, value):
        ''' to negate '''
        return self.real == value
