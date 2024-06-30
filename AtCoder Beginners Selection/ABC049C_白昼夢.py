s = input()

while s:
    if s.endswith('dream'):
        s = s[:-5]
    elif s.endswith('dreamer'):
        s = s[:-7]
    elif s.endswith('erase'):
        s = s[:-5]
    elif s.endswith('eraser'):
        s = s[:-6]
    else:
        print('NO')
        break

if not s:
    print('YES')
