#!/bin/python3

import math
import os
import random
import re
import sys

def checkWeird(n):
    if n % 2 != 0:
        return "Weird"
    if n >= 2 and n <= 5:
        return "Not Weird"
    if n >= 6 and n <= 20:
        return "Weird"
    if n > 20:
        return "Not Weird"

if __name__ == '__main__':
    N = int(input())
    print(checkWeird(N))
