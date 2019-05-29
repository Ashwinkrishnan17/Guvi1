n = int(input())
sum = 0
if(n != 0):
  sum = sum % 10 + sum * 10
  n = n / 10
  print("yes")
else:
  print("no")
