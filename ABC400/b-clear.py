N, M = map(int, input().split())

def sigma():
    global N, M
    result = 0

    for i in range(M+1):
        result += N**i

    if result <= 10**9:
        return result
    else:
        return "inf"

print(sigma())