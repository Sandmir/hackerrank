from collections import Counter
Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    rez = 1
    d_r = (Counter(list(b)))
    for k,i in d_r.items():
        if len(d_r) == 1 and k == '_':
            rez = 1
        elif len(d_r) == 1:
            rez = 0
        elif d_r.get('_') == None:
            rez = 1
            #проверим может уже все ок
            pair = 0
            b_t = b[0]
            for t in range(1,n):
                if b[t] == b_t:
                    pair += 1
                elif b_t != b[t]:
                    if pair <1:
                        rez = 0
                        break
                    pair = 0
                b_t = b[t]
        elif k != '_':
            if (i == 1):
                 rez = 0

    if rez == 0:
        print('NO')
    else:
        print('YES')


'''

__author__ = 'Senyutina'
from collections import Counter
Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    rez = 1
    d_r = (Counter(list(b)))

    if len(d_r) == 1 and d_r[0] == '_':
        rez = 1
    elif len(d_r) == 1:
        rez = 0
    elif d_r.get('_') == None:
         rez = 1
         pair = 0
         b_t = b[0]
         for t in range(1,n):
            if b[t] == b_t:
               pair += 1
            elif b_t != b[t]:
               if pair <1:
                    rez = 0
                    break
               pair = 0
               b_t = b[t]
    else:
        for k,i in d_r.items():
            if k != '_':
                if (i == 1):
                     rez = 0

    if rez == 0:
        print('NO')
    else:
        print('YES')
'''
'''
 print(len(d_r),k)
        if len(d_r) == 1 and k == '_':
            print('***')
            rez = 0
        elif k != '_':
            if (i == 1):
                 rez = 0

5
1
_
4
RBRB
4
RRRR
3
BBB
4
BBB_


YES
NO
YES
YES
YES




7
1
G
2
GR
4
_GR_
5
_R_G_
5
R_R_R
8
RRGGBBXX
8
RRGGBBXY


NO
NO
NO
NO
YES
YES
NO

'''
'''
from collections import Counter
Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    rez = 1
    d_r = (Counter(list(b)))
    for k,i in d_r.items():
        if len(d_r) == 1 and k == '_':
            rez = 1
        elif d_r.get('_') == None:
            rez = 1
            #проверим может уже все ок
            pair = 1
            b_t = b[0]
            for t in range(1,n):
                if b[t] == b_t:
                   pair += 1
                elif b_t != b[t]:
                    if pair <=1:
                        rez = 0
                        break
                    pair = 0
                b_t = b[t]
        elif k != '_':
            if (i == 1):
                 rez = 0

    if rez == 0:
        print('NO')
    else:
        print('YES')
'''
