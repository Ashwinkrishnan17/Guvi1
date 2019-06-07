n = int(input())
x = input().split()
y = []
for i in range(0,n):
  y.append(int(x[i]))
  c = sorted(y)
for j in c:
  print(j,end=" ")
