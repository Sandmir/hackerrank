__author__ = 'marina_senyutina'


t = int(input().strip())
for a0 in range(t):
    n,c,m = input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    ch = 0
    wr = (n//c)
    print('wr =',wr)
    ch +=wr
    while wr > 0:
         addPiece = wr//m,0
         wr = wr%m
         print('--  ',addPiece)
         ch += addPiece

         wr += addPiece*m

         print('ost', ch)
    # #     ch += addPiece
    #     print('ch',ch)
    # print(ch)
    #
    #
    #

