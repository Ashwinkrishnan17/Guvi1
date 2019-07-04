N = input()
a = []
list = []
for i in N:
  a.append(int(i))
a.append(int(a[0]))
for j in range(0,len(a) - 1):
  b = a[j] ** a[j + 1]
  list.append(b)
print(sum(list))
