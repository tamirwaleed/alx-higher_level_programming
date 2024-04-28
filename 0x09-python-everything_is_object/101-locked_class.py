#!/usr/bin/python3
""" Create a Locked Class """


class LockedClass:
    """ the class only allows first_name
    attribute """
    __slots__ = ["first_name"]
