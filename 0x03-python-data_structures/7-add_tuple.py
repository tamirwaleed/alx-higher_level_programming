#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tupa = tuple_a + (0, 0)
    tupb = tuple_b + (0, 0)
    tupc = tupa[0] + tupb[0], tupa[1] + tupb[1]
    return (tupc)
