N = input()
X_list = []
Y_list = []
for i in range(int(N)):
    X, Y = list(map(int, input().split()))
    X_list.append(X)
    Y_list.append(Y)

if sum(X_list) < sum(Y_list):
    print("Aoki")
elif sum(X_list) > sum(Y_list):
    print("Takahashi")
else:
    print("Draw")
