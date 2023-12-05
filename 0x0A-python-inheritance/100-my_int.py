#!/usr/bin/python3
''' REBELLION '''


class MyInt(int):
    ''' rebel child '''
    def __eq__(self, value):
        ''' to equate '''
        return self.value != value

    def __ne__(self, value):
        ''' to negate '''
        return self.value == value
