n = int(input())
c = []
a,b = 1,1
while(a < n):
  c.append(a)
  a,b = b,a + b
for i in c:
  print(i,end = " ")
