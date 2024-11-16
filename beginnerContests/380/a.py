n = list(input())

result = n.count('1') == 1 \
    and n.count('2') == 2 \
    and n.count('3') == 3

if result:
    print('Yes')
else:
    print('No')