def array_left_rotation(a, n, k):
   if k<n:
      a = a[k:] + a[:k]
   elif k > n:
      d = k%n
      a = a[d:] + a[:d]
   return a


n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')