
game_word = input()
l = len(game_word)
kevin_score,stuart_score = 0, 0
vowels = 'AEUIO'
for i in range(l):
    if game_word[i] in vowels:
       kevin_score += l - i
    else:
        stuart_score += l - i

if stuart_score > kevin_score:
    print("Stuart", stuart_score)
elif stuart_score < kevin_score:
    print("Kevin", kevin_score)
else:
    print("Draw")
'''

def find_substring(s,sub):
    count = 0
    for i in range(0, len(s)):
        count += s.count(sub,i,i+len(sub));
    return count

vowels = 'aeuioy'.upper()
game_word = input()
Strings: Making Anagrams

len_game = len(game_word)
stuart_score = 0
kevin_score = 0
stuart_words = []
kevin_words = []

for i, c in enumerate(list(game_word)):
    if c in vowels:
        for j in range(i, len_game+1):
            sub_str = game_word[i:j]
            if sub_str not in kevin_words and sub_str!= '':
                kevin_words.append(sub_str)
                kevin_score += find_substring(game_word,sub_str)
    else:
        for j in range(i, len_game+1):
            sub_str = game_word[i:j]
            if sub_str not in stuart_words and sub_str!= '':
                stuart_words.append(sub_str)
                stuart_score += find_substring(game_word,sub_str)


if stuart_score > kevin_score:
    print("Stuart", stuart_score)
elif stuart_score < kevin_score:
    print("Kevin", kevin_score)
else:
    print("Draw")
'''