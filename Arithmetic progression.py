n = int(input())
a = input().split()
N = int(a[0])
A = int(a[1])
D = int(a[2])
b = (N / 2) * ((2 * A) + ((N - 1) * D))
print(int(b))
