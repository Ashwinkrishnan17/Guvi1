a = int(input())
b = list(map(str,input().split()))
c = input()
count = 0
for i in b:
  for j in range(0,len(c) - 1):
    if(i[j] == c[j] and i[j + 1] == c[j + 1]):
      count = count + 1
print(count)
