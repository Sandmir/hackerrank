__author__ = 'marina_senyutina'

def is_leap(year):
    leap = False
    if (year%4 == 0):
      if (year%400==0):
          print('2')

          leap = True
      elif (year%100 == 0):
          leap = False
          print('3')

      else:
          leap = True
          print('4')

    return leap


year = int(input())
print(is_leap(year))
