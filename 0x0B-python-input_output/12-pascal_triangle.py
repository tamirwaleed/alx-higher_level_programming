#!/usr/bin/python3
''' Pascal Module '''


def pascal_triangle(n):
    ''' Pascal Function '''
    x = []
    bg = [[1]]
    if n <= 0:
        return x
    for i in range(2, n + 2):
        tmp = x[:]
        x.clear()
        for j in range(i):
            if j == 0 or j == i - 1:
                x.insert(j, 1)
            else:
                x.insert(j, int(tmp[j]) + int(tmp[j - 1]))
        if len(tmp) != 0:
            bg.append(tmp)
    return bg
