n = int(input())
a = list(map(int,input().split()))
b = []
for i in a:
  for j in range(0,i):
      b.append(j)
print(sum(b))
