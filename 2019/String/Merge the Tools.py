



s = input()
k = int(input())
d = int(len(s)/k)

for i in range(0,len(s),k):
    t = s[i:i+k]
    ns=''
    for j in t:
        if j not in ns and j!=' ':
            ns+=j
    print(ns)

