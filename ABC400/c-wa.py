import math

N = int(input())

def check():
    global N

    count = 0

    for i in range(N+1):
        num = i + 1

        if check_2(num) == True:
            count += 1
            # print(f"{num}: True")
        # else:
            # print(f"{num}: Flase")

    return count

def check_2(num):
    for b in range(1, int(math.isqrt(num)) + 1):
        b_squared = b**2

        if num % b_squared != 0:
            continue

        quotient = num // b_squared

        if quotient >= 2 and (quotient & (quotient - 1)) == 0:
            return True
        
    return False

print(check())