a = int(input())
b = list(map(int,input().split()))
for i in enumerate(b):
  if(i[0] % 2 == 0):
    if(i[1] % 2 != 0):
      print(i[1],end = " ")
  if(i[0] % 2 != 0):
    if(i[1] % 2 == 0):
      print(i[1],end = " ")
