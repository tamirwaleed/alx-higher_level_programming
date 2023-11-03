#!/usr/bin/python3
def calcu(argv):
    n = len(argv) - 1
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a, b = int(argv[1]), int(argv[3])
        if argv[2] == '+':
            print("{} + {} = {}".format(a, b, a + b))
        elif argv[2] == '-':
            print("{} - {} = {}".format(a, b, a - b))
        elif argv[2] == '*':
            print("{} * {} = {}".format(a, b, a * b))
        elif argv[2] == '/':
            print("{} / {} = {}".format(a, b, a / b))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)


if __name__ == "__main__":
    import sys
    calcu(sys.argv)
