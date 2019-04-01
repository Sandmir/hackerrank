__author__ = 'marina_senyutina'

import sys


n = int(input().strip())

for i in range(1,n+1):
     print((' '*(n-i)),'#'*i,sep='')
