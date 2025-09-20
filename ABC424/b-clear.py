N, M, K = map(int, input().split())

A = []
B = []

for i in range(K):
    a, b= map(int, input().split())
    A.append(a)
    B.append(b)

clear = [1 for _ in range(N)]
cleared = []

for i in range(K):
    clear[A[i]-1] += 1

    if clear[A[i]-1]-1 == M:
        cleared.append(A[i])

print(' '.join(map(str, cleared)))