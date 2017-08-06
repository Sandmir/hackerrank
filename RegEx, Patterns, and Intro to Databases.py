__author__ = 'Senyutina'

import sys


N = int(input().strip())
list_name = []
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    mail = emailID.split('@')
    if mail[1] == 'gmail.com':
       list_name.append(firstName)

for i in sorted(list_name):
    print(i)

'''
#!/bin/python3
import sys, re

names = []
pattern = re.compile('@gmail.com$')

N = int(input().strip())
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    if pattern.search(emailID):
        names.append(firstName)
names.sort()
for name in names:
    print(name)


**************************************
import sys
import re


gmail_first_names = []

N = int(input().strip())
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]

    m = re.search('@gmail.com', emailID)
    if m != None and emailID not in gmail_first_names:
        gmail_first_names.append(firstName)

gmail_first_names = sorted(gmail_first_names)
for each_name in gmail_first_names:
    print(each_name)


***************************

N = int(input().strip())
names = []
for a0 in range(N):
    firstName,emailID = input().strip().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if emailID.endswith('@gmail.com'):
        names.append(firstName)
names.sort()
print("\n".join(names))






'''