__author__ = 'marina_senyutina'
a = [int(c_temp) for c_temp in input().strip().split(' ')]
b = [int(c_temp) for c_temp in input().strip().split(' ')]

A = sum([1 for i in range(len(a)) if a[i]>b[i]])
B = sum([1 for i in range(len(a)) if a[i]<b[i]])
print(A, B)
