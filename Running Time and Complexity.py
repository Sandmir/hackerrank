__author__ = 'marina_senyutina'
import math

T = int(input())

for i in range(T):
    data = int(input())
    if data == 2:
        print('prime')
    elif data == 1:
        print('not prime')
    else:
        for i in range(2, math.ceil(math.sqrt(data)) + 1):
            if data % i == 0:
                print('not prime')
                break
        else:
            print('prime')