N = int(input())
a = list(map(int,input().split()))
count = 0
for i in range(0,len(a)):
  for j in range(0,len(a)):
    for k in range(0,len(a)):
      if(a[i] + a[j] == a[k] and i < j < k):\
        count = count + 1
print(count)
