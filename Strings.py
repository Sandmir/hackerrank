__author__ = 'Senyutina'
n = int(input())
w = len(bin(n)) - 2
for i in range(1, n + 1):
    print(str(i).rjust(w), oct(i)[2:].rjust(w), hex(i)[2:].upper().rjust(w), bin(i)[2:].rjust(w))
'''
#Designer Door Mat

N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in range(1,N,2):
    print((i*'.|.').center(M,'-'))
print('WELCOME'.center(M,'-'))
for i in range(N-2,-1,-2):
    print((i*'.|.').center(M,'-'))
'''
'''
9 27
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
'''

'''
#Text Alignment

#Replace all ______ with rjust, ljust or center.

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))


#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))

'''
'''
#String Validators

s = input()
is_an = is_a = is_d = is_l = is_u = False
for i in s:
    if i.isalnum() and is_an==False:
        is_an = True
    if i.isalpha()and is_a==False:
        is_a = True
    if i.isdigit()and is_d==False:
        is_d = True
    if i.islower()and is_l==False:
        is_l = True
    if i.isupper()and is_u==False:
        is_u = True

print(is_an)
print(is_a)
print(is_d)
print(is_l)
print(is_u)
#**********************
inp = input()
print(any(x.isalnum() for x in inp))
print(any(x.isalpha() for x in inp))
print(any(x.isdigit() for x in inp))
print(any(x.islower() for x in inp))
print(any(x.isupper() for x in inp))




'''
'''
#Find a string
s= input()
sub = input()
count = 0
for i in range(len(s)):
    t_s = s[i:i+len(sub)]
    if t_s == sub:
        count += 1
print(count)
'''
'''
I am an Indian, by birth.
Birth
0


ThIsisCoNfUsInG
is
1

'''