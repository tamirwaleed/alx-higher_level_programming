#!/usr/bin/python3
""" final module """


from sys import stdin


statuscodes = {"200": 0, "301": 0, "400": 0,
               "401": 0, "403": 0, "404": 0,
               "405": 0, "500": 0}

flsz = i = 0


def printstats():
    """ the function """
    print("File size: {}".format(flsz))
    for key, value in sorted(statuscodes.items()):
        print("{}: {}".format(key, value))


try:
    for line in stdin:
        splitted = line.split()
        if len(splitted) >= 2:
            flsz += int(splitted[-1])
            stcd = splitted[-2]
            if stcd in statuscodes:
                statuscodes[stcd] += 1
        i += 1
        if i > 10:
            printstats()
    printstats()
except KeyboardInterrupt:
    printstats()
