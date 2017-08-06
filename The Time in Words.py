__author__ = 'marina_senyutina'

import sys


h = int(input().strip())
m = int(input().strip())

numbers = {1: "one", 2: "two",   3: "three", 4: "four",  5: "five",
         6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
         11: "eleven",   12: "twelve",  13: "thirteen",   14: "fourteen",
         15: "fifteen",  16: "sixteen", 17: "seventeen",  18: "eighteen",
         19: "nineteen", 20: "twenty",  21: "twenty one", 22: "twenty two",
         23: "twenty three", 24: "twenty four",  25: "twenty five",
         26: "twenty six",   27: "twenty seven", 28: "twenty eight",
         29: "twenty nine"}

if m == 00:
    print(numbers[h], "o'clock")
elif m > 1 and m < 30 and m!=15:
    print(numbers[m], 'minutes past', numbers[h])
elif m == 15:
    print('quarter past', numbers[h])
elif m == 30:
    print('half past', numbers[h])
elif m == 1:
    print(numbers[m], 'minute past', numbers[h])
elif m == 45:
    print('quarter to', numbers[h+1])
else:
    print(numbers[60-m],'to', numbers[h+1])


