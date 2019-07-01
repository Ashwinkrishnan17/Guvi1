a = input()
b = []
for i in a:
  b.append(int(i))
c = str(sum(b))
if(c == c[::-1]):
  print("YES")
else:
  print("NO")
