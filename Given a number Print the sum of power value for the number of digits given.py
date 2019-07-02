a = input()
b = []
for i in a:
  b.append(int(i) ** len(a))
print(sum(b))
