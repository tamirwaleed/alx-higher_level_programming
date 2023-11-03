#!/usr/bin/python3
def infadd(argv):
    sum = 0
    if len(argv) == 0:
        print("{}".format(sum))
    else:
        for i in range(1, len(argv)):
            sum = sum + int(argv[i])
        print("{}".format(sum))


if __name__ == "__main__":
    import sys
    infadd(sys.argv)
