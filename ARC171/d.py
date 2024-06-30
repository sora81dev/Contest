def solve(P, B, N, M, queries):
    for i in range(1 << N):
        A = [int((i >> j) & 1) for j in range(N)]
        valid = True
        for query in queries:
            L, R = query
            s = A[L-1:R]
            hashed = sum(x * pow(B, len(s) - j - 1, P) for j, x in enumerate(s)) % P
            if hashed == 0:
                valid = False
                break
        if valid:
            return "Yes"
    return "No"

def main():
    P, B, N, M = map(int, input().split())
    queries = [list(map(int, input().split())) for _ in range(M)]
    result = solve(P, B, N, M, queries)
    print(result)

if __name__ == "__main__":
    main()
