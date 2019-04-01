def proverka(t):
    print(t)
    for j in range(len(t)):
        print(t[j])
        if sum(t[:j])+j > t[j]+1:
           return False
    return True

n = int(input())
x = [int(x_temp) for x_temp in input().strip().split(' ')]
rez = 0
for i in range(n):
    temp_x = x[i:]+x[:i]
    if proverka(temp_x):
       rez = i
       break
print(rez+1)
