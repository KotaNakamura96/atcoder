n, q = map(int, input().split())
numbers = [i for i in range(1, n + 1)]
offset = 0

for _ in range(q):
    queries = list(map(int, input().split()))
    if queries[0] == 1:
        p, x = queries[1:]
        numbers[(offset + (p - 1)) % n] = x
    elif queries[0] == 2:
        p = queries[1]
        print(numbers[(offset + (p - 1)) % n])
    else:
        k = queries[1]
        offset = (offset + k) % n
