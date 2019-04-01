
N = int(input())

S = list(input())


h = 0
pr_h = 0
v = 0
for i in S:

    if i == "U":
        h += 1
    else:
        h -= 1

    if pr_h == 0 and h == -1:
        v +=1
    pr_h = h

print(v)