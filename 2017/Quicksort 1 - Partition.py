__author__ = 'marina_senyutina'
n = int(input().strip())
arr = [int(c_temp) for c_temp in input().strip().split(' ')]
equal = arr[0]
left = []
right = []

for i in arr:
    if i > equal:
        right.append(i)
    elif i < equal:
        left.append(i)
        
print(" ".join(map(str,left)), equal," ".join(map(str,right)))



