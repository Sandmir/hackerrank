
def nod(a,b):
    if b > a:
        return nod(b, a)

    if a % b == 0:
        return b

    return nod(b, a % b)

def getTotalX(a, b):
    # Complete this function
    rez = []
    n = b[0]
    for i in range(len(b)-1):
        n = nod(n,b[i+1])
    print(n)
    for i in range(max(a),n):
        for j in a:
            if 

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
a = list(map(int, input().strip().split(' ')))
b = list(map(int, input().strip().split(' ')))
total = getTotalX(a, b)
'''print(total)'''
