def gcd(a,b):
  if(a == b):
    return a
  if(a > b):
    return gcd(a - b,b)
  return gcd(a,b - a)
def lcm(a,b):
  return (a * b) // gcd(a,b)
x,y = map(int,input().split())
print(lcm(x,y))
