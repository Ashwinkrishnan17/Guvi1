a = int(input())
b,c = map(int,input().split())
d = []
for i in range(b,c + 1):
  d.append(i)
for j in range(1,len(d) - 1):
  if(a == d[j]):
    print("yes")
    break
else:
  print("no")
