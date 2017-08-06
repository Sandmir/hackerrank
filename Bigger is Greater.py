__author__ = 'marina_senyutina'
q = int(input().strip())
for a0 in range(q):
    s = list(input().strip())
    print(s)
    arr = []
    for k in s:
        arr.append(ord(k))
    print(arr)
    n = len(s)
    r = 0
    for i in range(n-1):

       j = n-i-1
       if s[j]>s[j-1]:
          s[j],s[j-1] = s[j-1],s[j]
          print(''.join(s))
          r = 1
          break
    if r == 0:  print('no answer')