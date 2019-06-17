def gcd(x,y):
  if(x == y):
    return x
  if(x > y):
    return gcd(x - y,y)
  return gcd(x,y - x)
def lcm(x,y):
  return x * y // gcd(x,y)
a,b = map(int,input().split())
print(lcm(a,b))
