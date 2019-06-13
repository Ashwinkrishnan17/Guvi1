a = input()
b = []
for i in a:
  b.append(i)
for j in range(0,len(a),2):
  print(b[j],end = "")
print(end = " ")
for k in range(1,len(a),2):
  print(b[k],end = "")
