#!/bin/python3

import math
import os
import random
import re
import sys

def rev(array):
    array.reverse()
    print(*array, sep = ' ')

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    
    rev(arr)
