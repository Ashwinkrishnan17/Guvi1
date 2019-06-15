a = int(input())
b = input().split()
c = []
for i in b:
  c.append(int(i))
for j in range(0,len(c) - 1):
  if(c[j] > c[j + 1]):
    print(j)
 
