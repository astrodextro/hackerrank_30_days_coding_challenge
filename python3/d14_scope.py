class Difference:
    def __init__(self, a):
        self.__elements = a

	# Add your code here
    def computeDifference(self):
        a = self.__elements
        newlist = [abs(i-j) for i in a for j in a if i != j]
        if len(newlist) == 0:
            self.maximumDifference = 0
        else:
            self.maximumDifference = max(newlist)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)