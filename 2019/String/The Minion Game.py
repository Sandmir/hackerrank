
vowels = "AEOIU"

s = "BANANA"

stuart_score = 0
kevin_score = 0

len_s = len(s)

for i in range(len_s):
    if s[i] in vowels:
        kevin_score += len_s - i
    else:
        stuart_score += len_s - i

print(stuart_score)
print(kevin_score)
