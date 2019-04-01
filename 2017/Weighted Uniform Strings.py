__author__ = 'marina_senyutina'
import sys


s = input().strip()
n = int(input().strip())
letters = dict(zip('abcdefghijklmnopqrstuvwxyz', range(1, 27)))

print(letters)
m = 1
arr = []
pr = ''
v = 1
for i in s:
    if pr == i:
        m +=1
    else:
        m = 1
        v= letters.get(i)
        print(i,v)
    pr = i
    arr.append(m*v)
print(arr)
for a0 in range(n):
    x = int(input().strip())
    # your code goes here
    if x in arr:
        print('Yes')
    else:
        print('No')

'''
import sys


s = raw_input().strip()
n = int(raw_input().strip())
possible = set();

i = 0;
currChar = '';

while i < len(s):
    if s[i] != currChar:
        currCount = 0;
        currChar = s[i];

    currCount += 1;
    possible.add(currCount * (ord(currChar) - ord('a') + 1));

    i += 1;

for a0 in xrange(n):
    x = int(raw_input().strip());

    if x in possible: print "Yes";
    else: print "No";
    '''