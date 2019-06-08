a = input().split()
b = input().split()
for i in range(0,len(a)):
  c = int(a[i]) - int(b[i])
  print(abs(c),end = " ")
