__author__ = 'marina_senyutina'

def is_matched(expression):
    n = len(expression)
    for i in range(int(n//2)):
        if  (expression[i] == '[' and expression[n-1-i] != ']') or expression[i] == ']':
            return False
        elif (expression[i] == '{' and expression[n-1-i] != '}') or expression[i] == '}':
             return False
        elif (expression[i] == '(' and expression[n-1-i] != ')') or expression[i] == ')':
             return False
    return True



t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:

        print("NO")

'''
3
{[()]}
{[(])}
{{[[(())]]}}


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