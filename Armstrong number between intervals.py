a,b = input().split()
x = int(a)
y = int(b)
for i in range(x+1,y):
  temp = i
  sum = 0
  while(i != 0):
    a = i % 10
    sum = sum + a * a * a
    i = i // 10
  if(temp == sum):
   print(temp,end = " ")
