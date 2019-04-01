'''
1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0


-1 1 -1 0 0 0
0 -1 0 0 0 0
-1 -1 -1 0 0 0
0 -9 2 -4 -4 0
-7 0 0 -2 0 0
0 0 -1 -2 -4 0
'''


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)


count = ''
for x in range(1,5):
    for y in range(1,5):
        sum = arr[x-1][y-1]+arr[x-1][y]+arr[x-1][y+1] +arr[x][y] + arr[x+1][y-1]+arr[x+1][y]+arr[x+1][y+1]
        if count == '':
            count = sum
        if (sum>count):
            count = sum
print(count)
