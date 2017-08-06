__author__ = 'marina_senyutina'

y_cost = int(input())
s = input().strip().split(' ')
d = s[:len(s)-1]
m = int(d[0])
print(d)
for i in d:
    if int(i) < m and int(i)>=y_cost:
        m = int(i)

print(m-y_cost)

