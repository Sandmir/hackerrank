from itertools import product

s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = [int(keyboards_temp) for keyboards_temp in input().strip().split(' ')]
pendrives = [int(pendrives_temp) for pendrives_temp in input().strip().split(' ')]

max_c = -1
for i in list(product(keyboards,pendrives)):
    cost = i[0]+i[1]
    if cost <= s and cost > max_c:
        max_c =cost
        if max_c == s:
            break


print(max_c)




