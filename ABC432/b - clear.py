input = input()

def main(_input):

    sorted = list(_input)
    sorted.sort()

    if sorted[0] == '0':
        for i in range(len(sorted)):
            if sorted[i] != '0':
                sorted[0], sorted[i] = sorted[i], sorted[0]
                break

    return int("".join(sorted))


print(main(input))