N = int(input())

wins = [0] * N

for i in range(N):
    S = input().strip()
    for j in range(N):
        if i == j:
            continue 
        if S[j] == 'o':
            wins[i] += 1 

player_info = [(i + 1, wins[i]) for i in range(N)]
player_info.sort(key=lambda x: (-x[1], x[0]))  
for player, _ in player_info:
    print(player, end=' ')
