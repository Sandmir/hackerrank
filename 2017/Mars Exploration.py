__author__ = 'Senyutina'

mars = input()
n = int(len(mars)/3)
str_id = 'SOS'*n

print(sum(1 for i in range(len(mars)) if mars[i] !=  str_id[i]))