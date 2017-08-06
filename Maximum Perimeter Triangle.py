n = int(input())
arr = [int(e) for e in input().split(' ')]
tr = []
for i, a in enumerate(arr):
    for j, b in enumerate(arr):
        if i == j: continue
        for z, c in enumerate(arr):
            if (i == z) or (j == z): continue
            if (a < (b + c)) and (b < (c + a)) and (c < (a + b)):
                # print(a,b,c)
                tr.append([a, b, c])
m = 0
rex = []
for i in tr:
    if sum(i) > m:
        m = sum(i)
        rex = sorted(i)
        print('** ',m, rex)

myString = list( map(str,rex))
print(' '.join(myString))
print(tr)

# SOLUTIONS
'''
input()
a = list(map(int, input().split()))
a.sort(reverse=True)
for i in range(len(a) - 2):
    if a[i + 1] + a[i  + 2] > a[i]:
        print(a[i + 2], a[i + 1], a[i])
        exit()
print(-1)
'''

'''
from itertools import *
n = int(input())
l = sorted(map(int, input().split()))
ans = (-1, -1, -1)
for i, j, k in product(*repeat(range(n), 3)):
    if i < j < k and l[i] + l[j] > l[k]:
        ans = max(ans, (l[k], l[i], l[j]))
if ans[0] == -1:
    print(-1)
else:
    print(ans[1], ans[2], ans[0])
'''
'''
N = int(input())
L = sorted([int(n) for n in input().split()])

top = 0
for a in range(N):
    for b in range(N):
        for c in range(N):
            if a != b and a != c and b != c:
                test = sorted([a, b, c])
                testL = [L[n] for n in test]
                if testL[0] + testL[1] > testL[2]:
                    if sum(testL) > top:
                        top = sum(testL)
                        topl = testL
if top > 0:
    print(' '.join([str(n) for n in topl]))
else:
    print('-1')
'''

'''
N = int(input())
L = sorted([int(n) for n in input().split()])

top = 0
for a in range(N):
    for b in range(N):
        for c in range(N):
            if a != b and a != c and b != c:
                test = sorted([a, b, c])
                testL = [L[n] for n in test]
                if testL[0] + testL[1] > testL[2]:
                    if sum(testL) > top:
                        top = sum(testL)
                        topl = testL
if top > 0:
    print(' '.join([str(n) for n in topl]))
else:
    print('-1')
'''




'''
9 2015 5294 58768 285 477 72 13867 97 22445 48 36318 764 8573 183 3270 81 1251 59 95094
72 81 97



'''