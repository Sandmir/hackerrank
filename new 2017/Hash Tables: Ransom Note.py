from collections import Counter


def ransom_note(magazine, ransom):
    mag = dict(Counter(magazine))
    ransom = dict(Counter(ransom))
    for key in ransom:
        if mag[key] < ransom[key]:
            return False
    return True




m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if (answer):
    print("Yes")
else:
    print("No")