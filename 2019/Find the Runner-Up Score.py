

# n = int(input())
# arr = map(int, input().split())

arr = [57,57, -57, 57]

print(set(arr))

t = sorted(list(set(arr)))[-2]
print(t)