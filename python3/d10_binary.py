#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import groupby

def convertToBinary(n):
    binary = bin(n)
    binList = list(binary)
    repeats = list()
    del(binList[0])
    del(binList[0])
    bi = [len(list(g)) for k, g in groupby(binList, key=lambda x: x == "1") if k]
    print(max(bi))
    # for i in range(0, len(binList)):
    #     if b == "1":
    #         print(b)
    #         # repeats.append
    print(binList)
    

if __name__ == '__main__':
    n = int(input())
    convertToBinary(n)
