__author__ = 'Senyutina'
t = int(input().strip())
phone_dict = {}
for a0 in range(t):
    n, k = input().strip().split(' ')
    phone_dict[n] = k

for i in range(t):
    n = input().strip()
    if phone_dict.get(n) == None:
        print('Not found')
    else:
        print(phone_dict[n])

'''
n=int(input())

phonebook = dict(input().split() for _ in range(n))

for j in range(n):
    name = input().strip()
    if name in phonebook:
        print(name + "=" + phonebook[name])
    else:
        print("Not found")
'''