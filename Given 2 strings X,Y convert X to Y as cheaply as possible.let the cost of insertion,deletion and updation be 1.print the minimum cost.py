a,b = map(str,input().split())
x = list(a)
y = list(b)
d = abs(len(x) - len(y))
if(len(x) < len(y)):
    x = x + y[-d:]
else:
    y = y + x[-d:]
count = 0
for i in range(len(x)):
    if(x[i] != y[i]):
        y[i] = x[i]
        count = count + 1
print(count + d)
if(len(x) == 1):
    for i in x:
        if i in y:
            c = y.index(a)
            x = b[:c] + b[c] + b[c+1:]
            print(len(b[:c])+len(b[c+1:]))
elif(len(y) == 1):
    for i in y:
        if i in x:
            c = x.index(b)
            y = a[:c] + a[c] + a[c+1:]
            print(len(a[:c])+len(a[c+1:]))
