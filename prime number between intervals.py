a,b = input().split()
x = int(a)
y = int(b)
for i in range(x+1,y):
    if(i > 1):
        for j in range(2,(i//2 + 1)):
            if(i % j == 0):
                break
        else:
            print(i,end = " ")
