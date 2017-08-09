__author__ = 'marina_senyutina'
n = int(input().strip())

rezStr = ''
prevStr = []
for i in range(n):
    commands = input().split(' ')

    type_comm = commands[0]
    if type_comm !='4': temp_str = commands[1]

    if type_comm == '1':
        prevStr.append(rezStr)
        rezStr += temp_str
    elif   type_comm  == '2':
        prevStr.append(rezStr)
        rezStr = rezStr[:len(rezStr)-int(temp_str)]
    elif   type_comm  == '3':
        print(rezStr[int(temp_str)-1])
    elif   type_comm  == '4':
        rezStr = prevStr.pop()



    print('-- ',rezStr)
    print('//',prevStr)

    '''
        8
1 abc
3 3
2 3
1 xy
3 2
4
4
3 1
    '''