n, m = map(int, input().split())

indexes = []
for i in range(m):
    inputs = input().split()

    if int(inputs[0]) not in indexes and inputs[1] == 'M':
        indexes.append(int(inputs[0]))
        print('Yes')
    else:
        print('No')
