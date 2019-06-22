a = int(input())
b = list(map(int,input().split()))
c = []
for i,j in enumerate(b):
  if(i == j):
    c.append(i)
if(len(c) > 0):
  print(*c)
else:
  print("-1")
