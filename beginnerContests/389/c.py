from collections import deque

query_count = int(input())
snakes = deque()
total_shift = 0

for _ in range(query_count):
    queries = list(map(int, input().split()))
    if queries[0] == 1:
        length = queries[1]
        if not snakes:
            snakes.append([0, length])
        else:
            last_snake = snakes[-1]
            snakes.append([last_snake[0] + last_snake[1], length])
    elif queries[0] == 2:
        removed_snake = snakes.popleft()
        total_shift += removed_snake[1]
    elif queries[0] == 3:
        k = queries[1] - 1
        print(snakes[k][0] - total_shift)
