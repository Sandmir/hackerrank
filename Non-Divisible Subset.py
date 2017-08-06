n,k = input().strip().split(' ')
n,k = int(n),int(k)

n = 0
ost = []
for arr_temp in input().strip().split(' '):
    i = int(arr_temp)
    if i%k == 0:
        n = 1
    else:
        ost.append(i%k)
print(ost)
d = 0
if k == 2:
   if len(ost)>0: d = 1
else:
    i =  0
    while i < len(ost):
        p = ost[i]
        t = k - p
        if t in (ost[i:]):
           ind = ost[i:].index(t)+i
           ost.pop(ind)
        i+=1
    d = len(ost)

print(d+n)

'''
rez = list(ost)
for i in range(len(ost)):
    p = ost[i]
    t = k - p


    if t in (ost[i:]) and (t in rez) and (p in rez):
       rez.remove(t)
       print(p, ' = ', rez)

print(len(rez)+n%2, n)
'''



'''
for j in range(1,k//2+1):
   min_p = j
   max_p = k-j
   if  min_p in ost:
       while max_p in ost:
           ost.remove(max_p)
print(len(ost)+n)
'''

'''
__author__ = 'Senyutina'
n,k = input().strip().split(' ')
n,k = int(n),int(k)
arr = {int(arr_temp) for arr_temp in input().strip().split(' ')}
set_p = {}
rez = 0
for i in arr:
    p = {i}
    #print(p)
    set_p = arr - p
    #print(set_p)
    n = False
    for j in set_p:
        if (j+i)%k == 0:
            n = True
    if n == False:
       print(i)
       rez += 1

print(rez)
'''
'''
13 11
582740017 954896345 590538156 298333230 859747706 155195851 331503493 799588305 164222042 563356693 80522822 432354938 652248359
11

10 5
770528134 663501748 384261537 800309024 103668401 538539662 385488901 101262949 557792122 46058493
6

10 4
1 2 3 4 5 6 7 8 9 10
5


10 4
1 2 3 4 5 6 7 8 9 10

n,k = input().strip().split(' ')
arr = {int(arr_temp) for arr_temp in input().strip().split(' ')}
set_v = {}
for i in arr:
   set_v[i] = 0
   for j in arr:
       print('***', i, j)
       if i == j:
           pass
       elif (i+j)%int(k) != 0:
           print(i,j)
           set_v[i] += 1

rez = sum(1 for j in set_v.values() if j > 1)

print(rez)
print(set_v)
'''
'''
6 9
422346306 940894801 696810740 862741861 85835055 313720373
5

'''


'''
arr_temp = []
for i,c in enumerate(arr):
    for j in arr[i+1:]:
        if (c+j)%int(k) != 0:
            print(c,j)
            if c not in arr_temp:
               arr_temp.append(c)
            if j not in arr_temp:
               arr_temp.append(j)


print(len(set(arr_temp)))
'''

'''
13 11
582740017 954896345 590538156 298333230 859747706 155195851 331503493 799588305 164222042 563356693 80522822 432354938 652248359
11

6 9
422346306 940894801 696810740 862741861 85835055 313720373
5

n test case #7: Input: 10 4
1 2 3 4 5 6 7 8 9 10
Expected Output: 5
I am not getting this as there is subset of size 7: [1,2,4,5,6,9,10]

This initially appears difficult to solve in reasonable time complexity. After further thought, I think this can be done on O(n) with a few considerations. This is supposed to be an "easy" problem, so I'll provide some algorithm guidance here.

For any number K, the sum of 2 values (A & B) is evenly divisible by K if the sum of the remainders of A/K + B/K is K. (There is also a special case where both A & B are evenly divisible, giving a sum of 0.)

For any such remainder, there is 1 and only 1 other remainder value which will make a sum divisible by K.

Example: with K of 5, remainder pairs are 1+4 & 2+3. Given the numbers with a remainder of 1, they can't be paired with ANY of the numbers with remainder 4 (and vice versa). So, for the number of values in the resultant set, choose the larger of values with remainder 1 vs. values with remainder 4. Choose the larger set of remainder 2 vs remainder 3.

For the special case where remainder is 0, given the set of all values which are individually divisible by K, they can't be paired with any others. So, at most 1 value which is evenly divisible by K can be added to the result set.

For even values of K, the equal remainder is simular to the 0 case. For K = 6, pairs are 1+5, 2+4, 3+3. For values with remainder 3, at most one value can be added to the result set.

125 |
Add Comment Permalink

    pandross_1988 3 months ago

    Implementation in Python

    n, k = map(int,raw_input().strip().split(" "))

    arr = map(int,raw_input().strip().split(" "))

    d = {x:[] for x in range(k)}

    for i in range(n): d[arr[i]%k].append(arr[i])

    count = 0

    if len(d[0]) > 0:

    count = 1

    S = set([(x,k-x) for x in range(1,k//2+1)])

    for i,j in S:

    if i != j:

        if len(d[i]) > len(d[j]):

            count += len(d[i])

        else:

            count += len(d[j])

    else:

        if len(d[i]) > 0:

            count += 1

    print count

'''