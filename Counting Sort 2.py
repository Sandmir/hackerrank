__author__ = 'marina_senyutina'
n = int(input())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
s = ''
for i in range(100):
    s = s+ arr.count(i)*(str(i)+' ')

print(s)
