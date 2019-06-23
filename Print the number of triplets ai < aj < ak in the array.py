a = int(input())
b = list(map(int,input().split()))
c = []
e = []
for i in enumerate(b):
  c.append(i)
for i in range(0,len(b)):
  for j in range(0,len(b)):
    for k in range(0,len(b)):
      if(c[i][1] < c[j][1] < c[k][1]):
        if(c[i][0] < c[j][0] < c[k][0]):
          d = [c[i][1],c[j][1],c[k][1]]
          e.append(d)
if(len(e) != 0):
  print(len(e))
else:
  print("0")
