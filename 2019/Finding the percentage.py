# n = int(input())
student_marks = {'Test1': [25, 26.5, 28], 'Test2': [3.0, 9.0, 7.0], 'Test3': [3.0, 3.0, 3.0]}
# for _ in range(n):
#     name, *line = input().split()
#     scores = list(map(float, line))
#     student_marks[name] = scores
query_name = input()
print(sum(student_marks[query_name]))

print("%.2f" % round(sum(student_marks[query_name])/len(student_marks[query_name])))