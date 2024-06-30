H, W, N = map(int, input().split())
A = list(map(int, input().split()))

HW = H*W
if (HW > N):
    print("Yes")
else:
    print("No")