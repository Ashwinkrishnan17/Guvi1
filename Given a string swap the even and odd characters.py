a = input()
for i in range(0,len(a)):
  if(i % 2 != 0):
    print(a[i],end = "")
    print(a[i - 1],end = "")
