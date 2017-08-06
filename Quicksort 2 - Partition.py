__author__ = 'marina_senyutina'

def quick_sort(ar):
    if len(ar) < 2:
        return ar

    left = []
    right = []
    equal = []

    for i in ar:
        if i > ar[0]:
            right.append(i)
        elif i < ar[0]:
            left.append(i)
        else:
            equal.append(i)

    temp = quick_sort(left) + equal + quick_sort(right)
    print(*temp)
    return temp

n = int(input().strip())
arr = [int(c_temp) for c_temp in input().strip().split(' ')]

quick_sort(arr)


