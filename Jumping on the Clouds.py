__author__ = 'marina_senyutina'

n = int(input().strip())
c = [int(c_temp) for c_temp in input().strip().split(' ')]

step = 0
i = 0
while i < (n-1):
    step += 1
    if i == (n - 2) :break
    #step += 1
    if c[i+2] == 0:
        i = i +2
    else:
        i += 1
print(step)
