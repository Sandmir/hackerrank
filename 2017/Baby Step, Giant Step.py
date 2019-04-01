__author__ = 'Senyutina'

t = int(input().strip())
temp = [0]
for a0 in range(t):
    a, b, d = input().strip().split(' ')
    a, b, d = [int(a), int(b),int(d)]

    if d%a == 0:
        temp.append(d/a)
    elif d%b == 0:
        temp.append(d/b)
    elif d%(b+a) == 0:
        temp.append(d/(b+a))

    print(min(temp))
