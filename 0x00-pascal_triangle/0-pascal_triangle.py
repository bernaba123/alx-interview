#!/usr/bin/python3
"""
0-pascal_triangle.py
"""
import sys

def pascal_triangle(number):
    """
    print the triangle
    """
    ret = [[1]]
    for i in range(1, number):
        row = []
        for j in range(0, i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                res = ret[i-1][j-1]+ret[i-1][j]
                row.append(res)

        ret.append(row)
    return ret
