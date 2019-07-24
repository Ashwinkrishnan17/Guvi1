N,P,Q,R = map(int,input().split())
a = list(map(int,input().split()))
c = []
for i in range(0,len(a)):
  for j in range(0,len(a)):
    for k in range(0,len(a)):
      if(i <= j <= k):
        b = P*a[i] + Q*a[j] + R*a[k]
        c.append(b)
print(max(c))
