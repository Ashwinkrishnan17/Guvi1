a,b = map(int,input().split())
c = input().split()
list = []
count = 0
for i in c:
  list.append(int(i))
for j in range(0,len(c)):
  if(list[j] == b):
    count = count + 1
print(count)
