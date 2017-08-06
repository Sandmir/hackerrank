__author__ = 'Senyutina'
def array_left_rotation(a, n, k):
    if k < n:
       d = k
    else:
       d = k%n
    return  list(a[d:]+a[:d])

n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
