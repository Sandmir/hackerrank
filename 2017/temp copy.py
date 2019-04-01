import sys
import math

n = int(input().strip())
A = [int(A_temp) for A_temp in input().strip().split(' ')]
min_rez = - 1
for i,a in enumerate(A):
    for j,c in enumerate(A[i+1:]):
        if a == c:
            d = math.fabs(i-(j+i+1))
            if min_rez == -1: min_rez = d
            if d<min_rez: min_rez = d

print(int(min_rez))

'''
# Dummy solution in Python 3
s = input()
n = int(input())

len_s = len(s)
coun_s = s.count('a')
full_p = n//len_s * coun_s
part_p = s[:n%len_s+1].count('a')
print(full_p+part_p)
'''

'''
#Sock Merchant
n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]
color = set(c)
rez = sum(c.count(i)//2 for i in color if c.count(i)/2 >0)
print(rez)
'''

'''
n = input().strip()
T = list(set(int(x) for x in input().split()))
T.sort(reverse = True)
print(T)
'''
'''
#Bon Appetti
n,k = (input().strip().split(' '))
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
paid = int(input().strip())
a[k] = 0
res = sum(a)/2
if res == paid:
    print('Bon Appetit')
else:
    print(int(paid-res))
'''
'''
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = int(input())

x = sum(a) - a[k]
if 2 * b == x: print("Bon Appetit")
else: print(a[k] // 2)
'''
'''
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
s = ''
for i in range(n-1,-1,-1):
    s += str(arr[i]) +' '
print(s)

n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
r = arr[::-1]

for i in range(0,n):
    print (str(r[i]),end=" ")




n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for i in arr[::-1]:
    print (i, end=" ")

'''
'''
def diagonal(a):
   d = []
   o_d = []
   L = len(a)
   for i in range(L):
      d.append(a[i][i])
      o_d.append(a[L-i-1][i])
   return abs(sum(d)- sum(o_d))

n = int(input().strip())
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
    a.append(a_t)

print(diagonal(a))


n = int(input().strip())
for i in range(1,11):     print(i*n)
'''