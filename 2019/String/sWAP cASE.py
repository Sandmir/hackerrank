
# s.swapcase()

s = list("Pythonist 2")

for i in range(len(s)):

    ch = str(s[i])

    if ch.isupper():
        s[i] = ch.lower()
    else:
        s[i] = ch.upper()

print("".join(s))

s = "fkjdk"
s.rfind()