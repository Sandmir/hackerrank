import itertools

N = 4
S = "a a c d"
K = 2

arr = list(itertools.combinations(S.split(" "),K))

coun_a = sum([1 for t in arr if 'a' in t])
print(coun_a)