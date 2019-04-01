__author__ = 'Senyutina'

n = int(input().strip())
score_grade = {}
for a0 in range(n):
    record = input().strip().split(' ')
    last_name = record[0]
    grades = [float(x) for x in record[1:]]
    score_grade[last_name] = grades

rez_grade = score_grade[input()]
rez = sum(rez_grade)/len(rez_grade)
print('%.2f' % rez)

