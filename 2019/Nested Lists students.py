
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     students.append([name,score])


scores = [x[1] for x in students]
print(scores)
sc = sorted(list(set(scores)))[1]
print(sc)

sc_student = [s[0] for s in students if s[1]==sc]

print(sorted(sc_student))
