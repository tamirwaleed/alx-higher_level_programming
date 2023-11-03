#!/usr/bin/python3
def funno(argv):
    if len(argv) - 1 == 0:
        print("0 arguments.")
    elif len(argv) - 1 == 1:
        print("1 argument:\n1: {}".format(argv[1]))
    elif len(argv) - 1 > 1:
        print("{} arguments:".format(len(argv) - 1))
        for i in range(1, len(argv)):
            print("{:d}: {:s}".format(i, argv[i]))


if __name__ == "__main__":
    import sys
    funno(sys.argv)
