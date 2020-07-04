#!/bin/python3

import sys
                
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
output = list()
totalSwaps = 0

for i in range(0, len(a)):
    swaps = 0
    for j in range(0, len(a) - i -1):
        if a[j] > a[j+1]:
            # Perform swap
            a[j] = a[j] + a[j+1]
            a[j+1] = a[j] - a[j+1]
            a[j] = a[j] - a[j+1]
            swaps += 1
            
    if swaps == 0:
        break
    else:
        totalSwaps += swaps

# Print results
print("Array is sorted in {} swaps.".format(totalSwaps))
print("First Element: {}".format(a.pop(0)))
print("Last Element: {}".format(a.pop()))