a,b = input().split()
x = int(a)
y = int(b)
c = input().split()
sum = 0
for i in range(0,y,1):
  sum += int(c[i])
print(sum)
