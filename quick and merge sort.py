n = int(input())
a = input().split()
b = []
for i in range(0,n):
  b.append(int(a[i]))
  c = sorted(b)
for j in c:
  print(j,end=" ")
