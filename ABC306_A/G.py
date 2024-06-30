def is_possible_to_return(N, M, edges):
    # グラフの初期化
    graph = [[] for _ in range(N+1)]
    for u, v in edges:
        graph[u].append(v)

    # DFSによるトポロジカルソート
    visited = [False] * (N+1)
    stack = []
    def dfs(node):
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor)
        stack.append(node)

    dfs(1)
    sorted_order = stack[::-1]

    # 頂点1からのパスがあるか判定
    for node in sorted_order:
        if node == 1:
            return "Yes"
    return "No"


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v = map(int, input().split())
        edges.append((u, v))

    result = is_possible_to_return(N, M, edges)
    print(result)
