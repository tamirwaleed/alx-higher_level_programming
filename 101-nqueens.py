#!/usr/bin/python3
""" N Queen Module """


import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() == False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = boardinit(sys.arg[1])
    results = queensolve()
    for x in results:
        print(x)
