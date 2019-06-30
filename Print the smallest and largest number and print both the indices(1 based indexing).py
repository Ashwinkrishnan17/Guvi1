a = int(input())
b = list(map(int,input().split()))
print(b.index(min(b)) + 1,end = " ")
print(b.index(max(b)) + 1)
