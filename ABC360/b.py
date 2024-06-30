S, T = input().split(" ")

def test():
    global T, S
    try_count = 0

    c = 0
    w = 0
    list1 = []
    list2 = []
    str1 = ""

    if len(T) > len(S):
        return "No"
    
    if len(S) > 100:
        return "No"

    for w in range(len(S)-1):
        for c in range(len(S)-1):
            list2 = []
            str1 = ""
            list1 = [S[i:i+c+1] for i in range(0, len(S), c+1)]

            for i in range(len(list1)):
                if len(list1[i]) >= w+1:
                        temp = list(list1[i])
                        list2.append(temp[w])
            for i in range(len(list2)):
                str1 = str1 + list2[i]

            if str1 == T:
                if c <= w:
                    if w < len(S):
                        return "Yes"

    return "No"

print(test())