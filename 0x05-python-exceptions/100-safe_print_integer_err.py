#!/usr/bin/python3
def safe_print_integer_err(value):
    check = true
    try:
        print("{:d}".format(value))
        print()
    except TypeError as nope:
        print("Exception: {}".format(nope), file=sys.stderr)
        check = False
    except ValueError as nope:
        print("Exception: {}".format(nope), file=sys.stderr)
        check = False
    return (check)