n, m = map(int, input().split())
squares = [int(i) for i in input().split()]
stones = [int(i) for i in input().split()]

stones_total = sum(stones)
if stones_total != n:
    print(-1)
    exit

sorted_squares = sorted(squares)

available_move_counts = {}
for square, stone in zip(squares, stones):
    available_move_counts[square] = stone - 1

carry = 0
result = 0
previous = 1

for square in sorted_squares:
    gap = square - previous
    if gap > 0:
        if carry < gap:
            print(-1)
            exit()
        
        sum_moves = carry * gap - (gap * (gap + 1)) // 2
        result += sum_moves
        carry -= gap

    carry += available_move_counts[square]
    result += carry
    previous = square + 1

gap = n - previous + 1
if gap > 0:
    if carry < gap:
        print(-1)
        exit()
    sum_moves = carry * gap - (gap * (gap + 1)) // 2
    result += sum_moves
    carry -= gap

if carry != 0:
    print(-1)
else:
    print(result)
