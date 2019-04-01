
from collections import defaultdict

n,m = input().split(" ")
n,m = int(n),int(m)

A = []
B = []

for i in range(n):
    A.append(input())

for i in range(m):
    B.append(input())


d = defaultdict(list)
for i in range(len(A)):
    d[A[i]].append(i+1)

for i in B:
    if len(d[i]) == 0:
        print(-1)
    else:
        print(" ".join(str(s) for s in d[i]))
