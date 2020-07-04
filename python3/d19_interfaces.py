class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

from math import sqrt
from functools import reduce

class Calculator(AdvancedArithmetic):

    def divisorSum(self, n):
        output = set()
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                output.add(i)
                output.add(n // i)
        out = reduce(lambda x, y: x + y, output)
        return out


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)