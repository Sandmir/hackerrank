import collections

X = int(input())
Sizes = (list(map(int, input().split())))
N = int(input())
customer = list(list(map(int, input().split(" "))) for _ in range(N))

coll = dict(collections.Counter(Sizes))

earn = 0
for c in customer:
    if  (coll.get(c[0]) != None) and (coll.get(c[0]) > 0):
        earn += c[1]
        coll[c[0]] += -1

print(earn)