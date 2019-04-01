__author__ = 'marina_senyutina'

N, M = input().strip().split(' ')
N = int(N)
M = int(M)

arr = [0]*N
for i in range(M):
    a, b, k = [int(n) for n in input().split(" ")]
    arr[a-1] += k
    if b != N:
        arr[b] += -k

for i in range(1,N):
    s = arr[i-1]
    arr[i] += s
print(max(arr))


'''
5 3
1 2 100
2 5 100
3 4 100
'''