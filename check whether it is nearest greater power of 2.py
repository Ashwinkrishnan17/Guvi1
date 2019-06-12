a = int(input())
b = []
c = []
for i in range(0,a + 1):
  d = 2 ** i
  b.append(d)
for j in range(0,len(b)):
  if(b[j] == a):
    print(b[j + 1])
    break
else:
  for k in range(0,len(b)):
    if(a > b[k]):
      c.append(b[k + 1])
  print(max(c))
