__author__ = 'Senyutina'

n = int(input().strip())
score_grade = {}
for a0 in range(n):
    last_name = input().strip()
    grade = int(input().strip())
    score_grade[last_name] = grade

sort_grade = sorted(set(list(score_grade.values())))[1]
for i in sorted(score_grade):
    if i[1] == sort_grade:
        print(i[0])

'''
from collections import defaultdict
scores = defaultdict(list)
for i in range(int(input())):
    name = input()
    score = float(input())
    scores[score].append(name)
for name in sorted(scores[sorted(scores.keys())[1]]):print(name)
'''