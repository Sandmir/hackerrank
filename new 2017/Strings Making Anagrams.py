def number_needed(a, b):
    a1 = list(a)
    a2 = list(a)
    b1 = list(b)
    for i in range(len(a)):
       if a1[i] in b1:
           b1.remove(a1[i])
           a2.remove(a1[i])
    return  len(a2) + len(b1)

a = input().strip()
b = input().strip()

print(number_needed(a, b))

