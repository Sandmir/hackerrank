import sys

t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    a = [int(a_temp) for a_temp in input().strip().split(' ')]

    if sum([1 for a_temp in a if a_temp <= 0]) < k:
        print('YES')
    else:
        print('NO')    