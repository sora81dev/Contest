N=int(input())
A=list(map(int,input().split()))
#print(f"N:{N}   A:{A}")
status=0
for i in range(N):
    if A[i-1] != A[i]:
        status+=1
if status == 0:
    print("Yes")
else:
    print("No")