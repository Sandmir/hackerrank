__author__ = 'Senyutina'

t = int(input().strip())
for _ in range(t):
    n , k = input().strip().split(' ')
    n , k = int(n) , int(k)

    if ((k-1)|k) <= n:
        print(k-1)
    else:
        print(k-2)

'''
import itertools

t = int(input().strip())
for a0 in range(t):
    n, k = input().strip().split(' ')
    n, k = [int(n), int(k)]
    max_b = 0
    for i in itertools.combinations(range(1, n+1), 2):
        if max_b == k-1: break
        b_and = i[0]&i[1]
        if (b_and < k) and (max_b < b_and):
            max_b = b_and

    print(max_b)


'''