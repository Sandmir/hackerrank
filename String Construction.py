__author__ = 'Senyutina'
n = int(input().strip())
for a0 in range(n):
    s = input().strip()
    p = ""
    cost = 0
    print(s)
    for i in s:
        if i not in p:
            cost += 1
        p += i
print(cost)