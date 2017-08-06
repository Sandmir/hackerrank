__author__ = 'Senyutina'
import datetime

actualDay,actualMonth,actualYear = input().strip().split(' ')
actualDay,actualMonth,actualYear = [int(actualDay),int(actualMonth),int(actualYear)]

expectedDay,expectedMonth,expectedYear = input().strip().split(' ')
expectedDay,expectedMonth,expectedYear = [int(expectedDay),int(expectedMonth),int(expectedYear)]
fine = 0

d_a = datetime.date(actualYear,actualMonth,actualDay)
d_e = datetime.date(expectedYear,expectedMonth,expectedDay)
if d_a > d_e:
   if (actualYear - expectedYear) > 0:
       fine = 10000
   elif actualMonth - expectedMonth > 0:
       fine = (actualMonth - expectedMonth)*500
   elif actualDay - expectedDay >0:
       fine = (actualDay - expectedDay)*15

print(fine)