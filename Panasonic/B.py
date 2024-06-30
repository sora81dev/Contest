N = int(input())
A = list(map(int, input().split()))
for i in range(N):
    if i !=1:
        A[i-2]-A[i]