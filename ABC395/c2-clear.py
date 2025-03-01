N = int(input())
A = list(map(int, input().split()))

def check():
    last_index = {}
    min_len = float('inf')

    for i, value in enumerate(A):
        if value in last_index:
            min_len = min(min_len, i - last_index[value] + 1)
        last_index[value] = i

    return min_len if min_len != float('inf') else -1

print(check())
