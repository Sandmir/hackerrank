
n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
x = [int(x_temp) for x_temp in input().strip().split(' ')]

x = list(set(x))
x.sort()

st = 0
L = 1

while L != 0:
    min_x = min(x)
    temp_x = x.copy()

    for d in range((min_x+k),0,-1):
        if d in x:
            break
    print(x,d)
    for j in range(len(x)):
        print('** ',x[j])
        if x[j] > (d+k):
            break
        else  :
            print('-',x[j])
            temp_x.remove(x[j])
    x = temp_x
    st += 1
    if len(x) <= 1:
        L = 0
        st += len(x)
        break


print(st)
