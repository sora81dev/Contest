def main():
    n = int(input())
    # N の約数をすべて列挙する
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)

    # i が N/j の倍数となる最初の j を探す
    s = []
    for i in range(n + 1):
        for j in factors:
            if i % (n // j) == 0:
                s.append(str(j))
                break
        else:
            s.append('-')

    print(''.join(s))


if __name__ == '__main__':
    main()