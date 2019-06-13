a = input()
b = []
for i in a:
  b.append(int(i))
for j in range(0,len(b)):
  if(b[j] % 2 != 0):
    print(b[j],end = " ")
