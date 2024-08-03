N = 0
A = []
A_copy = []

N = int(input())
A = list(map(int, input().split()))

A_copy = sorted(A, reverse=True)

print(A.index(A_copy[1])+1)