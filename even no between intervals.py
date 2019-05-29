a,b = input().split()
x = int(a)
y = int(b)
for i in range(x+1,y):
  if(i % 2 == 0):
    print(i,end = " ")
