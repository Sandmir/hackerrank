__author__ = 'marina_senyutina'


def sort_insertion(arr1,n):
    ti = 0
    for j in range(2,n+1):
      arr = []
      arr = arr1[:j]
      temp = arr[j-1]
      for i in range(j-1,-1,-1):
          temp2 = arr[i-1]

          if (temp < temp2) and (i != 0):
              arr[i] = temp2
              ti += 1
          else:
              arr[i] = temp
          if arr[i] == temp: break

      arr1 = arr + arr1[j:]
    return ti
t = 0

def quick_sort_lom(ar, first, last):
    if first < last:
        p = partion(ar, first, last)
        quick_sort_lom(ar, first, p-1)
        quick_sort_lom(ar, p+1, last)



def partion(ar, first, last):
    global t
    pv = ar[last]
    i = first-1
    for j in range(first, last):

        if ar[j] <= pv:
            i += 1
            ar[i],ar[j] = ar[j],ar[i]
            t+=1
    print(*ar)

    ar[i+1],ar[last] = ar[last],ar[i+1]
    t+=1
    return i+1






n = int(input().strip())
arr1 = [int(c_temp) for c_temp in input().strip().split(' ')]
arr2 = list(arr1)
(quick_sort_lom(arr1,0, len(arr1)-1))
print(sort_insertion(arr2,n)-t)

