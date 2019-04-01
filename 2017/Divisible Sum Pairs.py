__author__ = 'Senyutina'


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
count = 0
for i, c in enumerate(a):
    for j in a[i+1:]:
        if (c+j)%k == 0:
            count += 1
            print(c,j)
print(count)