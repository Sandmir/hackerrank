

class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        from math import fabs

        d.maximumDifference = max(list(int(fabs(i-j)) for n,i in enumerate(self.__elements) for j in self.__elements[n:]))

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)