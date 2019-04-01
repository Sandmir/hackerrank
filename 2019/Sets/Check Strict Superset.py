
def subset_fun(A, sets):
    for s in sets:
        if s.issubset(A) == False:
            return False
    return True


A = set(input().split(" "))
n = int(input())

sets = []

for i in range(n):
    sub = set(input().split(" "))
    sets.append(sub)


print(subset_fun(A, sets))
