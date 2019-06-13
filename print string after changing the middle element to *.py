a = input()
b = []
for i in a:
  b.append(i)
if(len(b) % 2 != 0):
  c = len(b) // 2
  b[c] = "*"
else:
  c = len(b) //2
  b[c] = b[c - 1] = "*"
for j in b:
  print(j,end = "")
