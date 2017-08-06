
n = int(input().strip())
s = input().strip()
k = int(input().strip())
'''
alpha = list("abcdefghijklmnopqrstuvwxyz")
size = len(alpha)

temp = ''
for l in range(n):
    i = s[l].lower()
    if i == '-':
        h = i
    else:

        if alpha.index(i) + k > size:
           g =  alpha.index(i) + k - size
        else:
           g = alpha.index(i) + k
        h = alpha[g]
        if s[l].islower():
           h = h.lower()
        else:
           h = h.upper()

    temp += h
print(temp)

'''
spec = ['!','_','/','^','-','<','>','*','(',')','&','.','#','$','%','0','1','2','3','4','5','6','7','8','9','`','?','{','}','[',']']
temp = ''
for i in s:
    ind = ord(i.lower())
    if i  in spec:
        h = i
    else:
        if k > 26 : k = k%26
        if ind+k > 122:
            g = ind+k-122+96
        else:
            g = ind + k
        h = chr(g)
        if i.isupper(): h = h.upper()
    temp += h
print(temp)

WGYcqh?u5a*5<EPuzl6?O5t3Fp.1aZ)io1OPj4(!pnWS3Z)kbLC.VfNc9p7Zse?OrxC2wBIXP4ZRP*lvM8(oan9pVkpj!7xrthr.
WGYcqh?u5a*5<EPuzl6?O5{3F].1aZ)io1OPj4(!][WS3Z)kbLC.VfNc9]7Zse?OrxC2wBIXP4ZRP*lvM8(oan9pVk]j!7xrthr.

