a = int(input())
b = []
for i in range(0,a):
  i = list(input())
  b.append(i)
c = zip(*b)
c = list(c)
for i in c:
  if(i.count(i[0]) == len(i)):
    print(i[0],end = "")
  else:
    break
