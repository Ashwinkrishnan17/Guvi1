a,b = map(int,input().split())
c = []
for i in range(a,b + 1):
  count = 0
  for j in range(2,i + 1):
    if(i % j == 0):
      count = count + 1
  c.append(count)
print(c.count(1))
