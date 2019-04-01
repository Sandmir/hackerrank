__author__ = 'marina_senyutina'

import sys

exm = 'hackerrank'
q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    # your code goes here
    rez = True
    for i in exm:
        t = s.find(i)
        if t != -1:
            s = s[t + 1:]
        else:
            rez = False
            break

    if False == rez:
        print('NO')
    else:
        print('YES')