a = input()
b = a.lower()
c = []
for i in range(97,123):
  if(chr(i) not in a):
    print("no")
    break
else:
  print("yes")
