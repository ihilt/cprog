#!/usr/bin/env python3

import math
import os
import random
import re
import sys

magic_pattern = [ [8, 1, 6], [3, 5, 7], [4, 9, 2] ]

def rotate(arr):
    new_arr = [[0,0,0],[0,0,0],[0,0,0]]
    new_arr[0][0] = arr[2][0]
    new_arr[0][1] = arr[1][0]
    new_arr[0][2] = arr[0][0]
    new_arr[1][0] = arr[2][1]
    new_arr[1][1] = arr[1][1]
    new_arr[1][2] = arr[0][1]
    new_arr[2][0] = arr[2][2]
    new_arr[2][1] = arr[1][2]
    new_arr[2][2] = arr[0][2]
    return new_arr

def flip_y(arr):
    new_arr = [[0,0,0],[0,0,0],[0,0,0]]
    new_arr[0] = arr[2]
    new_arr[1] = arr[1]
    new_arr[2] = arr[0]
    return new_arr

def flip_x(arr):
    new_arr = [[0,0,0],[0,0,0],[0,0,0]]
    new_arr[0][0] = arr[0][2]
    new_arr[0][1] = arr[0][1]
    new_arr[0][2] = arr[0][0]
    new_arr[1][0] = arr[1][2]
    new_arr[1][1] = arr[1][1]
    new_arr[1][2] = arr[1][0]
    new_arr[2][0] = arr[2][2]
    new_arr[2][1] = arr[2][1]
    new_arr[2][2] = arr[2][0]
    return new_arr

def checkFit(arr):
    patterns = []
    patterns.append(magic_pattern)
    patterns.append(flip_x(magic_pattern))
    patterns.append(flip_y(magic_pattern))
    patterns.append(rotate(rotate(magic_pattern)))
    patterns.append(rotate(flip_x(magic_pattern)))
    patterns.append(rotate(magic_pattern))
    patterns.append(rotate(rotate(rotate(magic_pattern))))
    patterns.append(rotate(flip_y(magic_pattern)))

    costs = [0, 0, 0, 0, 0, 0, 0, 0]
    i = 0

    while i < len(patterns):
        cost = 0
        r = 0
        while r < 3:
            c = 0
            while c < 3:
                if arr[r][c] != patterns[i][r][c]:
                    costs[i] += abs(arr[r][c] - patterns[i][r][c])
                c += 1
            r += 1
        i += 1
    return min(costs)

def formingMagicSquare(s):
    return checkFit(s)

if __name__ == '__main__':
    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    print(result)
