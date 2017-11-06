
def is_matched(expression):

    d = {'(' :')', '{' :'}', '[' :']'}
    stack = []
    for i in expression:
       if d.get(i):
           stack.append(d[i])
       else:
           if len(stack ) ==0 or (i != stack[-1]):
               return False
           stack.pop()

    return len(stack) == 0

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")


'''
5
}][}}(}][))]
[](){()}
()
({}([][]))[]()
{)[](}]}]}))}(())(



NO
YES
YES
YES
NO
'''
