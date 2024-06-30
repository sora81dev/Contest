def min_cost_for_eggs(N, S, M, L):
    pack_prices = [S, M, L]

    min_cost = float("inf")
    for i in range(N // 6 + 1):
        for j in range(N // 8 + 1):
            k = max((N - i * 6 - j * 8 + 11) // 12, 0)
            total_cost = i * pack_prices[0] + j * pack_prices[1] + k * pack_prices[2]
            total_eggs = i * 6 + j * 8 + k * 12
            if total_eggs >= N:
                min_cost = min(min_cost, total_cost)

    return min_cost


N, S, M, L = map(int, input().split())

result = min_cost_for_eggs(N, S, M, L)
print(result)
