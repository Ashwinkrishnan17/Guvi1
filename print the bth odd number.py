a,b = map(int,input().split())
c = input().split()
if(int(c[b]) % 2 == 0):
  print(int(c[b - 1]))
else:
  print(int(c[b]))
