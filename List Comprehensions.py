__author__ = 'Senyutina'

N = int(input())

X = [x for x in range(int(input())+1)]
Y = [y for y in range(int(input())+1)]
Z = [z for z in range(int(input())+1)]
rez = []
for x in X:
    for y in Y:
        for z in Z:
            if (x + y +z) != N:
                rez.append([x,y,z])

print(X)
print(rez)

'''
X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

X += 1
Y += 1
Z += 1

tmp_list = [[x, y, z] for x in range(X) for y in range(Y) for z in range(Z) if x + y + z != N]
print(tmp_list)



//////////////////////////////////////////////////////////////////////////////
xr = range(int(input())+1)
yr = range(int(input())+1)
zr = range(int(input())+1)
n = int(input())

arr = [[x, y, z] for x in xr for y in yr for z in zr if x+y+z != n]
print(arr)

'''