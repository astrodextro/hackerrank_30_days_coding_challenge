#!/bin/python3

import math
import os
import random
import re
import sys


def printMultiples(n):
    for i in range(1, 10+1):
        print("{} x {} = {}".format(n, i, n*i))


if __name__ == '__main__':
    n = int(input())
    printMultiples(n)
