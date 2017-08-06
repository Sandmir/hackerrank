__author__ = 'marina_senyutina'
import sys

def solve(grades):
    # Complete this function
    for i in range(0,n):
        if grades[i] >= 38:
           nr =  grades[i]//5*5+5
           os = nr - grades[i]
           if os < 3:  grades[i] = nr
    return grades
n = int(input().strip())
grades = []
for grades_i in range(0,n):
    grades_t = int(input().strip())
    grades.append(grades_t)
result = solve(grades)
print(result)