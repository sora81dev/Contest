def solve(N, Q, A, queries):
    results = []
    
    for b, k in queries:
        distances = [abs(a - b) for a in A]
        distances.sort()
        results.append(distances[k - 1])
    
    return results

import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
Q = int(data[1])

A = list(map(int, data[2:N+2]))
queries = []
index = N + 2

for i in range(Q):
    b = int(data[index])
    k = int(data[index + 1])
    queries.append((b, k))
    index += 2

results = solve(N, Q, A, queries)

for result in results:
    print(result)
