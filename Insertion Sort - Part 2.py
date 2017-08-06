__author__ = 'marina_senyutina'

n = int(input().strip())
arr1 = [int(c_temp) for c_temp in input().strip().split(' ')]

for j in range(2,n+1):
  arr = []
  arr = arr1[:j]
  temp = arr[j-1]
  for i in range(j-1,-1,-1):
      temp2 = arr[i-1]
      if (temp < temp2) and (i != 0):
          arr[i] = temp2
      else:
          arr[i] = temp
      if arr[i] == temp: break

  arr1 = arr + arr1[j:]
  print(" ".join(map(str,arr1)))


'''
6
1 4 3 5 6 2
'''


