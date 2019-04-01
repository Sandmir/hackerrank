__author__ = 'marina_senyutina'
s = input()
n = 1
while n == 1:
  n = 0
  for i in range(len(s)-1):
      print(s[i])
      if s[i] == s[i+1]:
          print("= ",s[i:i+2])
          s = s.replace(s[i:i+2],'')
          print('// ',s)
          n = 1
          break

print(s)