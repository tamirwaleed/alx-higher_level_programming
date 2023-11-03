#!/usr/bin/python3
def calcu(argv):
    n = len(argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a, b = argv[1], argv[3]
        if argv[2] == '+':
            print("{} + {} = {}".format(a, b, int(a) + int(b)))
        elif argv[2] == '-':
            print("{} - {} = {}".format(a, b, int(a) - int(b)))
        elif argv[2] == '*':
            print("{} * {} = {}".format(a, b, int(a) * int(b)))
        elif argv[2] == '/':
            print("{} / {} = {}".format(a, b, int(a) / int(b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)


if __name__ == "__main__":
    import sys
    calcu(sys.argv)
