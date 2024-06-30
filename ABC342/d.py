from collections import defaultdict

def is_square(num):
    root = int(num ** 0.5)
    return root * root == num

def count_square_pairs(N, A):
    square_roots = defaultdict(int)
    count = 0
    
    for i in range(N):
        if is_square(A[i]):
            square_roots[A[i]] += 1
    
    for i in range(N):
        for square_root in square_roots:
            if A[i] != square_root and A[i] * square_root in square_roots:
                count += square_roots[A[i] * square_root]
    
    return count // 2

# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))

# 答えを出力
print(count_square_pairs(N, A))
