a,b,c = input().split()
x = int(a)
y = int(c)
if(b == "/"):
  z = x // y
  print(z)
else:
  z = x % y
  print(z)
