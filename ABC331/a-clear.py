def next_date(M, D, y, m, d):
    d += 1
    if d > D:
        d = 1
        m += 1
        if m > M:
            m = 1
            y += 1
            if y > 9000:
                y = 1000

    return y, m, d


M, D = map(int, input().split())
y, m, d = map(int, input().split())

result = next_date(M, D, y, m, d)

print(*result)
