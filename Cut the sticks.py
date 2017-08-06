__author__ = 'Senyutina'


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]

res = n
while res > 0:
    print(res)
    arr1 = [min(arr)]*len(arr)
    arr = list(map(lambda x,y: x-y,arr,arr1))
    arr = [arr_temp for arr_temp in arr if arr_temp > 0]
    res = len(arr)




'''
step = min(arr)
arr1 = [step]*len(arr)
arr = list(map(lambda x,y: x-y,arr,arr1))
count = 0
print(arr)
print(sum(1 for i in arr if i >0))
for i, c in enumerate(arr):
    if c <=0:
       arr.pop(i)


print((arr))
'''