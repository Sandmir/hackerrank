__author__ = 'marina_senyutina'

s = input().capitalize()
rez = []
pr_s = ' '
for i in str(s):

    if pr_s == ' ' and i != pr_s:
        t = i.upper()
        rez.append(t)
    else:
        rez.append(i)
    pr_s = i

print(''.join(rez))


'''

n = int(input())
str_al = 'abcdefghijklmnopqrstuvwxyz'
s = str_al[:n]

wight = n*3
print(wight)

for i in s[::-1]:
    print(i)



'''