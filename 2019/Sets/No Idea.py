n,m = input().split(" ")
n,m = int(n),int(m)

arr = set(list(input().split(" ")))
print(arr)

set_a = set(list(input().split(" ")))
set_b = set(list(input().split(" ")))

print(sum([(arr[i] in set_a ) - (arr[i] in set_b) for i in range(len(arr))]))
