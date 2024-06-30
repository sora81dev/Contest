n = int(input())
a = list(map(int, input().split()))

x = [0] * n
for i in range(n):
    while a[i] % 2 == 0:
        x[i] += 1
        a[i] //= 2

print(min(x))