import sys

def find_ex(s, k):
    arr = []

    l = len(k)
    for i in range(len(s)-1):

        if s[i:i+l] == k:
            arr.append(i)


    if arr != []:
        return arr
    else:
        return None


t = int(input().strip())
for a0 in range(t):
    R,C = input().strip().split(' ')
    R,C = [int(R),int(C)]
    G = []
    G_i = 0
    for G_i in range(R):
       G_t = str(input().strip())
       G.append(G_t)
    r,c = input().strip().split(' ')
    r,c = [int(r),int(c)]
    P = []
    P_i = 0
    for P_i in range(r):
       P_t = str(input().strip())
       P.append(P_t)

    print(G)
    print(P)
    f= P[0]
    for i in range(G):
        g = G[i]
        arr = find_ex(i,f)
        if arr != None:
            print('Yes',arr)
            for j in arr:





'''
2
10 10
7283455864
6731158619
8988242643
3830589324
2229505813
5633845374
6473530293
7053106601
0834282956
4607924137
3 4
9505
3845
3530
15 15
400453592126560
114213133098692
474386082879648
522356951189169
887109450487496
252802633388782
502771484966748
075975207693780
511799789562806
404007454272504
549043809916080
962410809534811
445893523733475
768705303214174
650629270887160
2 2
99
99





1
4 4
1234
1234
1234
1234
2 2
23
23
'''