a = int(input())
b = list(map(int,input().split()))
c = sorted(b)
d = c[::-1]
e = []
for i in range(0,len(b)):
  e.append(d[i])
  e.append(c[i])
for j in e[:len(b)]:
  print(j,end = " ")
