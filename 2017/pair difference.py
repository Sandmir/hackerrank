import sys

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

res_a = sum(map(lambda x,y: 1 if x > y else 0, a,b))
res_b = sum(map(lambda x,y: 1 if x < y else 0, a,b))
print(res_a,res_b)

