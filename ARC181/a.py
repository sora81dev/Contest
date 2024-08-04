def count_inversions(arr):
    inversions = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                inversions += 1
    return inversions

def min_operations(arr):
    inversions = count_inversions(arr)

    return -(-inversions // (len(arr) - 1)) 

test_cases=[]

T = int(input())
for i in range(T):
    N = int(input())
    test_cases.append(list(map(int, input().split())))
for arr in test_cases:
    print(min_operations(arr.copy()))