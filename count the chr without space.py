a = input()
count = 0
for i in a:
  if(i == " "):
    count = count + 1
counter = len(a) - count
print(counter)
