from collections import namedtuple

N,headers = int(input()), input().split()
Student =  namedtuple('Student',headers)

sum_marks = 0
for i in range(N):
    v = input().split()
    student = Student(*v)
    sum_marks += int(student.MARKS)

print(sum_marks/N)

'''

5
ID MARKS NAME CLASS
1 97 Raymond 7
2 50 Steven 4
3 91 Adrian 9
4 72 Stewart 5
5 80 Peter 6

'''