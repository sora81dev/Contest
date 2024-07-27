def find_final_position(H, W, Si, Sj, grid, X):
    x, y = Si - 1, Sj - 1
    
    moves = {
        'L': (0, -1),
        'R': (0, 1),
        'U': (-1, 0),
        'D': (1, 0)
    }
    
    for move in X:
        dx, dy = moves[move]
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < H and 0 <= ny < W and grid[nx][ny] == '.':
            x, y = nx, ny

    return x + 1, y + 1

# 標準入力から値を読み込む
H, W = map(int, input().split())
Si, Sj = map(int, input().split())
grid = [input().strip() for _ in range(H)]
X = input().strip()

x, y= find_final_position(H, W, Si, Sj, grid, X)

print(f"{x} {y}")