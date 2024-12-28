a, b, c = map(int, input().split())

if a == b == c:
    print('Yes')
else:
    if a + b == c or a + c == b or b + c == a:
        print('Yes')
    else:
        print('No')