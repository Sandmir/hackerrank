
m, n = map(int, input().strip().split(' '))
l = input().strip().split(' ')
A = set(input().strip().split(' '))
B = set(input().strip().split(' '))

temp = {}
for i in l:
    temp[i] = temp.get(i,0) + 1
happiness = 0
for k,v in temp.items():
    if k in A:
        happiness += v
    elif k in B:
        happiness -= v

print(happiness)
