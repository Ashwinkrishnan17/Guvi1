a,b = map(int,input().split())
c = list(map(int,input().split()))
d = []
for i in range(0,b):
  i = list(map(int,input().split()))
  d.append(i)
for i in d:
  e = c[i[0] - 1:i[1]]
  f = e[0]
  for j in range(0,len(e) - 1):
    f = f ^ e[j + 1]
  print(f)
