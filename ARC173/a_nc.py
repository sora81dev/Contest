def is_neq_number(x):
    s = str(x)
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True

def generate_neq_numbers(k):
    count = 0
    i = 1
    while count < k:
        if is_neq_number(i):
            count += 1
        i += 1
    return i - 1

def main():
    t = int(input())
    for _ in range(t):
        k = int(input())
        print(generate_neq_numbers(k))

if __name__ == "__main__":
    main()
