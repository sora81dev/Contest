S = input()

def find_different_chars(s):
    char_count = {}
    for i, char in enumerate(s):
        if char in char_count:
            char_count[char].append(i)
        else:
            char_count[char] = [i]

    for char, positions in char_count.items():
        if len(positions) == 1:
            print(positions[0]+1)

find_different_chars(S)
