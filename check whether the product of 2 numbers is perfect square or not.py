a,b = map(int,input().split())
c = a * b
d = c ** (1/2)
e = d * d
if(e == c):
  print("yes")
else:
  print("no")
