a = input()
b = a.lower()
for i in range(97,123):
  if(chr(i) not in a):
    print("no")
    break
else:
  print("yes")
