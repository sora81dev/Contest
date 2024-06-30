import math

# 各リールの文字列と文字列の長さを読み取る
M = int(input())
reels = []
for i in range(3):
    Si = input()
    Mi = len(Si)
    reels.append((Si, Mi))

# 各リールの文字列の長さからLCMを計算する
LCM = reels[0][1]
for i in range(1, 3):
    LCM = (LCM * reels[i][1]) // math.gcd(LCM, reels[i][1])

# 各リールを止めるために必要な時間を計算する
times = []
for i in range(3):
    time_i = (LCM // reels[i][1]) * reels[i][1] - (LCM % reels[i][1])
    times.append(time_i)

# 全てのリールが同じ文字を示すか確認
if all(reels[i][0] == reels[0][0] for i in range(1, 3)):
    answer = 0
else:
    answer = -1

# 最大の時間が回答
print(answer)
