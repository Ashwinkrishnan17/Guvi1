a,b,c = input().split()
x = int(a)
y = int(b)
z = int(c)
if(x > y):
  if(x > z):
    print(x)
  else:
    print(z)
elif(y > z):
  print(y)
else:
  print(z)
