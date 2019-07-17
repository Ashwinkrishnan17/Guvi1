a = input()
b = a.lower()
for i in range(97,123):
  if(chr(i) not in b):
    print("no")
    break
else:
  print("yes")
