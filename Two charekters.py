
import sys


s_len = int(input().strip())
s = input().strip()

arr = list(set(s))
print(arr)
max = 0
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
       a,b = arr[i],arr[j]
       s1 = ''
       for t in s:
           if t == a or t == b:
              s1 += t
       print('==',s1)
       '''validation'''
       v = True
       for k in range(len(s1) -1):
           print(s1[k],s1[k+1])
           if s1[k] == s1[k+1]:
               v = False
               print(v)

       if v == True and max < len(s1):
           max = len(s1)
print(max)

