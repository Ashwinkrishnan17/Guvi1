N = int(input())
a = list(map(int,input().split()))
for i in range(0,len(a)):
  for j in range(0,len(a)):
    if(a[i] + a[j] == 0 and i < j):
      print(a[i],a[j])
