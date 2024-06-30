MOD = 998244353

def count_inversions(A):
    n = len(A)
    BIT = [0] * (n + 1)
    total_inversions = 0

    def update(idx, val):
        while idx <= n:
            BIT[idx] += val
            BIT[idx] %= MOD
            idx += idx & -idx

    def query(idx):
        result = 0
        while idx > 0:
            result += BIT[idx]
            result %= MOD
            idx -= idx & -idx
        return result

    for i, a in enumerate(A):
        total_inversions += i - query(a)
        total_inversions %= MOD
        update(a, 1)

    return total_inversions

def solve(N, A):
    inversions = count_inversions(A)
    if inversions % 2 == 0:
        return pow(2, N - 1, MOD)
    else:
        return 0

def main():
    N = int(input())
    A = list(map(int, input().split()))
    result = solve(N, A)
    print(result)

if __name__ == "__main__":
    main()
