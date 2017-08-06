__author__ = 'marina_senyutina'


N, Q = input().strip().split(' ')
N, Q = [int(N), int(Q)]

S = [[]] * N

lastAns = 0
for m in range(Q):
    a = [int(a_temp) for a_temp in input().strip().split(' ')]
    i, x, y = a[0],a[1],a[2]
    k = (x ^ lastAns) % N
    if i == 1:
        S[k] = S[k] + [y]
    elif i == 2:
        num = y%len(S[k])
        lastAns = S[k][num]
        print(lastAns)




'''
2 5
1 0 5
1 1 7
1 0 3
2 1 0
2 1 1
'''