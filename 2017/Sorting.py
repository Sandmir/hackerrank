__author__ = 'Senyutina'

import sys


n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]

swap = 0
for i in range(1, n):
    f = 0
    for j in range(0, n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            f = 1
            swap += 1
    if f == 0: break

print('Array is sorted in', swap, 'swaps.')
print('First Element:', a[0])
print('Last Element:', a[n - 1])

