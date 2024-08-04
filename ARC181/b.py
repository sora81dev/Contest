def check_match(S, T, X, Y):
    def generate_string(S, T, pattern):
        res = ""
        for bit in pattern:
            res += S if bit == '0' else T
        return res

    generated_X = generate_string(S, T, X)
    generated_Y = generate_string(S, T, Y)

    return generated_X == generated_Y

def find_T(S, X, Y):
    max_len = max(max(len(sub) for sub in X.split('0')), max(len(sub) for sub in Y.split('0')))
    for i in range(len(S) - max_len + 1):
        T = S[i:i+max_len]
        if check_match(S, T, X, Y):
            return "Yes"
    return "No"

t = int(input())
S, X, Y = [], [], []
for _ in range(t):
    S.append(str(input()))
    X.append(str(input()))
    Y.append(str(input()))
    
for i in range(t):
    #print(f"{i} S:{S[i]}  X:{X[i]}  Y:{Y[i]}")
    print(find_T(S[i], X[i], Y[i]))
