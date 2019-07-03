N = input()
a = []
for i,j in enumerate(N):
  b = int(j) ** i
  a.append(b)
print(sum(a))
