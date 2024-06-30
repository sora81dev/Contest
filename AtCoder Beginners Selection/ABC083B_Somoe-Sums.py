n,a,b=map(int,input().split())
2
def digit_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n //= 10
    return s

def solve(N, A, B):
    ans = 0
    for i in range(1, N+1):
        if A <= digit_sum(i) <= B:
            ans += i
    return ans

print(solve(n,a,b))