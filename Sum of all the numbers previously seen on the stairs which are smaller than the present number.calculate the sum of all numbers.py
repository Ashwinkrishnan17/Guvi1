n = int(input())
a = list(map(int,input().split()))
b = []
for i in range(1,len(a)):
  c = a.index(a[i])
  d = a[:c]
  for j in d:
    if(j < a[i]):
      b.append(j)
print(sum(b))
