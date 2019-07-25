n = int(input())
d = []
g = []
for i in range(2 ** n):
  a = bin(i)[2:]
  b = len(a)
  c = str(0) * (n - b) + a
  d.append(c)
for i in d:
  e = i.count("1")
  f = (e,i)
  g.append(f)
for i in sorted(g):
  print(i[1])
