#!/usr/bin/env python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    rows = len(arr)
    cols = len(arr[0])

    x1 = y1 = 0
    pd = 0
    while x1 < cols and y1 < rows:
        pd += arr[y1][x1]
        y1 += 1
        x1 += 1

    y1 = rows - 1
    x1 = 0
    sd = 0
    while x1 < cols and y1 > -1:
        sd += arr[y1][x1]
        y1 -= 1
        x1 += 1
    return abs(pd - sd)

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
