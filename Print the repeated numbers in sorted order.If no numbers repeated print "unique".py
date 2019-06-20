from collections import Counter
a = int(input())
b = list(map(int,input().split()))
c = Counter(b)
list = []
for i in c.items():
  if(i[1] != 1):
    print(i[0],end = " ")
for j in c.items():
  list.append(j[1])
if(max(list) == 1):
  print("unique")
