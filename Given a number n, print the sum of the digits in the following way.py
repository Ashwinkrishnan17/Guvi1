n = input()
a = []
b = []
for i in range(0,len(n)):
  a.append(n[0:i + 1])
for i in a:
  for j in i:
    b.append(int(j))
print(sum(b))
