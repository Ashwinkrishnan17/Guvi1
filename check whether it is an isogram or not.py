a = input()
b = sorted(a)
for i in range(0,len(a) - 1):
  if(b[i] == b[i + 1]):
    print("No")
    break
else:
  print("Yes")
