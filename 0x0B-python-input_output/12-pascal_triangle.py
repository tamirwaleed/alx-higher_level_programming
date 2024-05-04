#!/usr/bin/python3
""" returns a list of pascal triangle """


def pascal_triangle(n):
    """ n is the triangle level """
    pasc = []
    lev = []
    if n <= 0:
        return pasc
    else:
        for i in range(n):
            temp = lev[:]
            lev = [1]
            for j in range(1, i + 1):
                if j == i:
                    lev.append(1)
                else:
                    lev.append(temp[j] + temp[j - 1])
            pasc.append(lev)
    return pasc[:]
