a,b = map(int,input().split())
c = list(map(int,input().split()))
list = []
for i in c:
  if(i % 2 != 0):
    list.append(i)
print(list[b - 1])
