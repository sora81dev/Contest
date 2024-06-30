N = int(input())
S = input()
Q = int(input())
CD = []
for i in range(Q):
    CD.append(input())

def rc(arr, tc, rc):
    return arr.replace(tc, rc)

for i in range(Q):
    new_rc=rc(S, CD[i][1],CD[i][2])
    S=new_rc

print(S)