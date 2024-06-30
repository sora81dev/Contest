n = int(input())

prev_t, prev_x, prev_y = 0, 0, 0

for i in range(n):
    t, x, y = map(int, input().split())
    distance = abs(x - prev_x) + abs(y - prev_y)
    if (t - prev_t) % 2 != distance % 2 or distance > t - prev_t:
        print('No')
        break
    prev_t, prev_x, prev_y = t, x, y
else:
    print('Yes')
