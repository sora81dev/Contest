N, M = input().split()
N_i, M_i = int(N), int(M)
A = list(map(int, input().split()))

def main(N, M, A):
    if sum(A) <= M:
        return "infinite"
    
    count = 1
    while 1:
        now = 0

        for i in range(N):
            now = now + min(count, A[i])

        if now >= M:
            return count-1
        
        count += 1


print(main(N_i, M_i, A))
