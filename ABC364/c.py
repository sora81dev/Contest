def main(N, X, Y, A, B):
    dishes = list(zip(A, B))

    dishes.sort(key=lambda dish: dish[0] + dish[1])

    total_sweetness = 0
    total_saltiness = 0

    count = 0
    for sweetness, saltiness in dishes:
        total_sweetness += sweetness
        total_saltiness += saltiness
        count += 1
        if total_sweetness > X or total_saltiness > Y:
            break
    
    return count
N, X, Y = input().split()

N_i = int(N)
X_i = int(X)
Y_i = int(Y)
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(main(N_i, X_i, Y_i, A, B))