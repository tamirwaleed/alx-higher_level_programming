#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    check = True
    try:
        print("{:d}".format(value))
    except TypeError as nope:
        print("Exception: {}".format(nope), file=sys.stderr)
        check = False
    except ValueError as nope:
        print("Exception: {}".format(nope), file=sys.stderr)
        check = False
    return (check)
