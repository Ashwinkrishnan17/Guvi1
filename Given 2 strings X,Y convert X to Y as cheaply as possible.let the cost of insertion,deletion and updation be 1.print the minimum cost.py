x,y = map(str,input().split())
a = list(x)
b = list(y)
l1 = len(a)
l2 = len(b)
c = abs(l1 - l2)
if(l1 < l2):
  a = a + b[-c:]
else:
  b = b + a[-c:]
count = 0
for i in range(len(a)):
  if(a[i] != b[i]):
    a[i] = b[i]
    count = count + 1
print(count + c)
