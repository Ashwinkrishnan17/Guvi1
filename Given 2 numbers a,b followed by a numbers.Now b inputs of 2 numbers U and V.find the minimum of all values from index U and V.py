a,b = map(int,input().split())
c = list(map(int,input().split()))
d = []
for i in range(0,b):
  i = list(map(int,input().split()))
  d.append(i)
for i in d:
  x = min(c[i[0] - 1:i[1]])
  print(x)
