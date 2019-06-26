from collections import Counter
a = int(input())
b = list(map(int,input().split()))
c = Counter(b)
for i in c.items():
  if(i[1] == 1):
    print(i[0])
