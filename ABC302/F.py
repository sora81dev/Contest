class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1


def can_create_target_set(N, M, sets):
    uf = UnionFind(M)

    for i in range(N):
        a = sets[i][0]
        b = sets[i][1:]

        uf.union(a, b[0])

    if uf.find(1) == uf.find(M):
        return True
    else:
        return False


# 入力例
N,M=map(int,input().split())
queries=[]
for _ in range(N):
    query=list(map(int,input().split()))
    queries.append(query)
result = can_create_target_set(N, M, queries)
print(result)
