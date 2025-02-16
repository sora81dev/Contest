import sys
from collections import defaultdict

def solve():
    N, M = list(map(int, input().split()))
    
    edge_count = defaultdict(int)
    removed_edges = 0

    for _ in range(M):
        u, v = map(int, sys.stdin.readline().split())
        
        if u == v:
            removed_edges += 1
            continue
        
        key = (min(u, v), max(u, v))
        edge_count[key] += 1

    for key in edge_count:
        removed_edges += edge_count[key] - 1

    print(removed_edges)

solve()