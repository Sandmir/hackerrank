from builtins import print

__author__ = 'marina_senyutina'


import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

plus = 0.0
minus = 0.0
zero = 0.0

for i in arr:
    if i > 0:
        plus +=1
    elif i < 0:
        minus +=1
    else: zero += 1

print(float(plus)/n)
print(minus/n)
print(zero/n)