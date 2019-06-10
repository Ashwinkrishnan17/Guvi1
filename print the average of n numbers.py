n = int(input())
a = input().split()
b = []
for i in a:
  b.append(int(i))
c = sum(b) // n
print(c)
