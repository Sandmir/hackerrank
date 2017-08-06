__author__ = 'Senyutina'

n = int(input().strip())

commands = []
for i in range(n):
    commands.append(input())

new_list = []
for comm in commands:
    c = comm.split(' ')
    if c[0] == 'insert':
        new_list.insert(int(c[1]),int(c[2]))
    elif c[0] == 'pop':
        new_list.pop()
    elif c[0] == 'print':
        print(new_list)
    elif c[0] == 'remove':
        new_list.remove(int(c[1]))
    elif c[0] == 'append':
        new_list.append(int(c[1]))
    elif c[0] == 'sort':
        new_list.sort()
    elif c[0] == 'revese':
        new_list.reverse()

'''
n = input()
l = []
for _ in range(n):
    s = raw_input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print l
'''