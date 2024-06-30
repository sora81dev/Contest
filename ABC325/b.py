# 入力
N = int(input())
locations = []

for _ in range(N):
    W, X = map(int, input().split())
    start_time = max(9, X)
    end_time = min(18, X + 1)
    locations.append((start_time, end_time, W))

time_slots = [0] * 24
for start, end, W in locations:
    for i in range(start, end):
        time_slots[i] += W

max_attendance = max(time_slots)

print(max_attendance)
