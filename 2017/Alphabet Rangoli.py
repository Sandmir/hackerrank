
n = int(input())
str_al = 'abcdefghijklmnopqrstuvwxyz'
s = str_al[:n][::-1]
wight = (n-1)*4 +1

for i in range(1,n+1):
    l = '-'.join(s[:i])
    l_r = str(l+l[::-1][1:])
    print(l_r.center(wight,'-'))

for i in range(1,n):
    l = '-'.join(str_al[:n][i:])
    l_r = str(l[::-1][:len(l)-1]+l)
    print(l_r.center(wight,'-'))


