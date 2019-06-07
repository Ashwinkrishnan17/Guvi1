n = int(input())
a = input().split()
i = 0
if(int(a[i]) > int(a[i+1])):
  if(int(a[i]) > int(a[i+2])):
    print(a[i])
  else:
    print(a[i+2])
elif(int(a[i+1]) > int(a[i+2])):
  print(a[i+1])
else:
  print(a[i+2])
