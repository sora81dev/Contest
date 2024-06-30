from collections import defaultdict

def max_ball_types(N, AB, UV):
    graph = defaultdict(list)
    for u, v in UV:
        graph[u].append(v)
        graph[v].append(u)

    max_types = [0] * (N + 1)  # 各頂点までの最大種類数を保存するリスト

    def dfs(node, parent):
        types = set()  # 種類数を保持する集合
        types.add(AB[node][0])  # ボールAの種類を追加
        types.add(AB[node][1])  # ボールBの種類を追加

        for neighbor in graph[node]:
            if neighbor == parent:
                continue
            child_types = dfs(neighbor, node)
            types |= child_types  # 子ノードの種類数を追加

        max_types[node] = len(types)  # 最大種類数を更新
        return types

    dfs(1, -1)  # 頂点1を根としてDFSを実行

    return max_types[2:]  # 結果を返す

# 入力を受け取る
N = int(input())
AB = [list(map(int, input().split())) for _ in range(N)]
UV = [list(map(int, input().split())) for _ in range(N-1)]

# 問題を解く
result = max_ball_types(N, AB, UV)

# 結果を出力
print(*result)
