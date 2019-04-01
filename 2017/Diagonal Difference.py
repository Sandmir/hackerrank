

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

s_d1 = sum([a[i][i] for i in range(n)])
s_d2 = sum([a[i][n-i-1] for i in range(n)])

print(abs(s_d1-s_d2))

'''
3
11 2 4
4 5 6
10 8 -12
'''