# A - Strictly Increasing?

N = int(input())
A = list(map(int, input().split()))

def check():
    global N, A
    
    for i in range(N-1):
        if A[i] >= A[i+1]:
            return "No"
        
    return "Yes"

print(check())