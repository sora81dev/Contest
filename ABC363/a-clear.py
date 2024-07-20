R = int(input())

def main(R):
    if 1 <= R <= 99:
        return 100-R
    elif 100<= R <= 199:
        return 200-R
    elif 200 <= R <= 299:
        return 300-R
    
    return 0

print(main(R))