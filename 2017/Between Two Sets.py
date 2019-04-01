__author__ = 'Senyutina'
import sys


n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]

if 0 in a:
    print(0)
else:
    min_b = min(b)
    max_b = max(b)
    max_a = max(a)
    min_a = min(a)
    temp = []
    for i in range(max_a, min_b + 1):
        nod = True
        for j in b:
            if j % i != 0:
                nod = False
                break
        if (nod == True) and (i not in temp):
            temp.append(i)


    rez = []
    for t in temp:
        tm = True
        for i in a:
            if t % i != 0 :
               tm = False
               break
        if tm == True and t not in rez:
            rez.append(t)
    print(rez)
    print(len(rez))