a = input().split()
b = []
for i in a:
  if(i.istitle()):
    b.append(i)
if(len(b) == len(a)):
  print("yes")
else:
  print("no")
