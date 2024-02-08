#!/usr/bin/python3
''' pascal triangle '''


def pascal_triangle(n):
    ''' the function '''
    emp = [[]]
    temp1 = []
    if n <= 0:
        return temp1
    for i in range(n):
        temp = []
        for j in range(0, i + 1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(temp1[j - 1] + temp1[j])
        temp1 = temp[:]
        emp.append(temp1)
    return emp[1:]
