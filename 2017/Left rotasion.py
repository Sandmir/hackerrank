__author__ = 'marina_senyutina'
n, d = input().strip().split(' ')
n, d = [int(n), int(d)]
arr = [int(a_temp) for a_temp in input().strip().split(' ')]

print(" ".join(map(str,(arr[d:] +arr[:d]))))