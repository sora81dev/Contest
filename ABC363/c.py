from itertools import permutations

N, K = input().split()
N_i, K_i = int(N), int(K)
T = str(input())

st = set()
for it in permutations(T):
    st.add("".join(it))

sort_st = sorted(st)


def consencutive_chars(T, A):
    count = 1
    for i in range(len(T)):
        if not i == 0:
            if T[i] == T[i-1]:
                count += 1
                if count == A:
                    return True
                
            else:
                count = 1

    return False

def is_palindrome(s):
    return s == s[::-1]


result = len(sort_st)

for i in range(len(sort_st)):
    if consencutive_chars(sort_st[i], K_i) or is_palindrome(sort_st[i]):
        result -= 1

print(result)