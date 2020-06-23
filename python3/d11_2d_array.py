#!/bin/python3

import math
import os
import random
import re
import sys

def getHourglassSum(arr):
    result = []
    rows = len(arr)
    for i, d1 in enumerate(arr):
        if i > rows - 3:
            break
        cols = len(d1)
        for j, d2 in enumerate(d1):
            if j > cols - 3:
                break
            a = arr[i][j]
            b = arr[i][j+1]
            c = arr[i][j+2]
            d = arr[i+1][j+1]
            e = arr[i+2][j]
            f = arr[i+2][j+1]
            g = arr[i+2][j+2]
            result.append(a+b+c+d+e+f+g)
    print(max(result))

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    getHourglassSum(arr)
