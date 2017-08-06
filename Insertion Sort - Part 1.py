__author__ = 'marina_senyutina'

n = int(input().strip())
arr = [int(c_temp) for c_temp in input().strip().split(' ')]
temp = arr[n-1]
for i in range(n-1,-1,-1):
    temp2 = arr[i-1]
    if (temp < temp2) and (i != 0):
        arr[i] = temp2
    else:
        arr[i] = temp
    print(" ".join(map(str,arr)))
    if arr[i] == temp: break



