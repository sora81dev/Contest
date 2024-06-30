def calculate_f(A, K):
    B = sorted(A, reverse=True)[:K]
    return sum(B)

N, K, Q = map(int, input().split())
A = [0] * N

for _ in range(Q):
    X, Y = map(int, input().split())
    A[X - 1] = Y
    print(calculate_f(A, K))
