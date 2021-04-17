import random
s="abcdefghij"
for i in range(4):
  a=random.choice(s)
  print(a, end="  ")
  s = s.replace(a,"")
