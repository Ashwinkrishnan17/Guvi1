a = int(input())
b =[]
for i in range(0,a):
  i = list(map(int,input().split()))
  b.append(i)
merge = []
for i in b:
  merge = merge + i
c = sorted(merge)
for i in c:
  print(i,end = " ")
