a,b = map(int,input().split())
c = input().split()
list = []
for i in c:
  list.append(int(i))
for j in range(0,len(c)):
  if(list[j] == b):
    print("yes")
    break
else:
  print("no")
