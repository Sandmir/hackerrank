
import sys
'''
n = int(input().strip())
s = str(bin(n))

print(len(max(s[2:].split('0'))))
'''
#si.split('0')
#print(si)
#print(len(max(si)))

'''
time = input().strip().upper()
L = len(time)

if time[L-2::1] == 'PM':
    hour = time[2:]
    if hour == '12':
        hour = '00'
    else: hour = int(time[:2])+12)
    new_time = str(int(time[:2])+12) + time[2:L-2]
else: new_time = time[:L-2]
print(new_time)


n = int(input().strip())
arr = []
for i in range(n):
    arr.append(input())

print(arr)
'''

def sum_arr(ar):
    if ar == []:
        return 0
    else:
        return ar[0] + sum_arr(ar[1:])

arrr = [1,2,3,20]
print(sum_arr(arrr))
