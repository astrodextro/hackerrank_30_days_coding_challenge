#!/bin/python3

import os
import sys

#
# Complete the stoneDivision function below.
#
def stoneDivision(n, s):
    #
    # Write your code here.
    #
    players = ["First", "Second"]
    pilesList = [n]
    iterations = 0

    s = list(filter((1).__ne__, s))
    s = list(set(map(lambda x: x, s)))
    
    while True:
        newPilesList = performDivision(pilesList, s)
        if newPilesList == None:
            break
        iterations += 1
        pilesList = newPilesList
    
    winningPlayerIndex = (iterations + 1) % 2
    print(players[winningPlayerIndex])
    return players[winningPlayerIndex]

def performDivision(pilesList, divisorsSet):
    # Iterate through pile set
    for pile in pilesList:
        # for each stone set check for divisibility by any of the number set
        for divisor in divisorsSet:
            quotient = pile / divisor
            # Check pile is equally divided by divisor
            if quotient.is_integer():
                # Create new set from division of pile
                newPilesList = [quotient] * divisor
                # Remove divided item
                pilesList.remove(pile)
                # Add sub items
                newPilesList += pilesList
                # Return new list
                return newPilesList
    # Return losing player
    return None
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    s = list(map(int, input().rstrip().split()))

    result = stoneDivision(n, s)
    
    fptr.write(result + '\n')

    fptr.close()
