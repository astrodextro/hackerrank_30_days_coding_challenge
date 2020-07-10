from math import sqrt

class Solution():
    def __init__(self):
        self.values = []

    def insert(self, value):
        self.values.append(value)

    def testPrimality(self):
        for value in self.values:
            if value == 1:
                print("Not prime")
            elif value == 2 or value == 3:
                print("Prime")
            elif value % 2 == 0 or value%3 == 0:
                print("Not prime")
            else:
                n = 0
                for i in range(5, int(sqrt(value)) + 1):
                    if value%i == 0 or value%(i+2) == 0:
                        n += 1
                        break
                if n > 0:
                    print("Not prime")
                else:
                    print("Prime")
                


T=int(input())
sol=Solution()
root=None
for i in range(T):
    val=int(input())
    sol.insert(val)
sol.testPrimality()
