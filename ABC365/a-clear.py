def main(y):
    if not y%4 == 0:
        return 365
    
    if y%4 == 0 and not y%100 == 0:
        return 366
    
    if y%100 == 0 and not y%400 == 0:
        return 365
    
    if y%400 == 0:
        return 366
    
Y = int(input())
print(main(y=Y))