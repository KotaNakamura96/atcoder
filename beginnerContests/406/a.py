a, b, c, d = map(int, input().split())

if a < c:
    print('No')
elif a > c:
    print('Yes')
elif b < d:
    print('No')
else:
    print('Yes')