a = input()
list = []
for i in a:
  list.append(int(i))
for j in range(0,len(list)):
  if(list[j] % 2 != 0):
    print(list[j],end = " ")
