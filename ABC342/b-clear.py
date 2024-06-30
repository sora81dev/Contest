N = int(input())
P = list(map(int, input().split()))
Q = int(input())
AB = []
A = []
B = []
for i in range(Q):
    AB = list(map(int, input().split()))
    A.append(AB[0])
    B.append(AB[1])

def funp(arr, target):
    for i, num in enumerate(arr):
        if num == target:
            return i

for i in range(Q):
    index_a = funp(P, A[i])
    index_b = funp(P, B[i])
    if index_a < index_b:
        print(P[index_a])
    else:
        print(P[index_b])