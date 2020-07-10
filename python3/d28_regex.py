#!/bin/python3

import math
import os
import random
import re
import sys

class Database():
    def __init__(self):
        self.db = []
    
    def insert(self, firstName, emailID):
        self.db.append({
            "name": firstName,
            "email": emailID
        })

    def performRexex(self):
        ls = []
        for item in self.db:
            if re.search(".*@gmail.com$", item["email"]):
                ls.append(item["name"])
        ls.sort()
        print("\n".join(ls))


if __name__ == '__main__':
    N = int(input())
    db = Database()

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]

        db.insert(firstName, emailID)
    db.performRexex()
        
