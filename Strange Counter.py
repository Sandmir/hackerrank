__author__ = 'Senyutina'
'''
t = int(input().strip())

time = 1
value = 3

while t >= time + value:
    time += value
    value *= 2

print(value - (t - time))
'''
t = int(input())
Sn, n = 0, 0
while Sn < t:
    n += 1
    Sn += 3 * 2 ** (n - 1)
print(Sn - t + 1)
'''
t = int(input().strip())
N = 3
back_counter = 3

for i in range(1,t):
    #print(i,back_counter)
    back_counter -= 1
    if  back_counter == 0:
        back_counter = N * 2
        N *= 2

print(back_counter)
'''
'''
1000000000000
649267441662
'''

'''
rem = 3
while t > rem:
    t = t-rem
    rem *= 2

print(rem-t+1)

'''