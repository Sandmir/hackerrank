__author__ = 'marina_senyutina'
import sys


c = [int(c_temp) for c_temp in input().strip().split(' ')]
s = sum(c)
print(s-max(c),s-min(c))