__author__ = 'Senyutina'

s = input().strip()
t = input().strip()
k = int(input().strip())
l = len(s)

if s==t and k>l*2 :
    print('Yes')
elif k >= l + len(t):
    print('Yes')
else:

    temp = 0
    for i in range(l,0,-1):
        s1 = s[0:i]
        t1 = t[0:i]

        if s1 == t1:
            temp = l-i
            break
    print(s1)
    if k-temp == len(t) - len(t1):
       print('Yes')
    elif (k-temp > len(t) - len(t1)) and (len(t) - len(t1))%2 == 0:
        print('Yes')
    else:
       print('No')

'''
hackerhappy
hackerrank
9
'''