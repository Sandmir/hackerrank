#N = input()

#s = map(lambda x: print(x+1,sep= '', end='',),range(int(N)))
#print(s)
#map(lambda x: print('***'),[1,2,3,4])
#print(*range(1, int(N)+1), sep='')

#f = lambda x: print(x, sep='')

#map(f,[1,2,3])

#list(map(lambda x: print(x,end=''), range(1,int(input())+1)))


from random import randint

print('5')  # No. of Test cases for testing the Problem

case = "Yes"
for i in range(5):
    n = randint(1, 200)
    k = randint(1, n)

    print(n, k)