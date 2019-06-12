a = int(input())
b = []
for i in range(2,a):
  b.append(i)
for j in range(0,len(b)):
  if(a % b[j] == 0):
    print("no")
    break
else:
  print("yes")
