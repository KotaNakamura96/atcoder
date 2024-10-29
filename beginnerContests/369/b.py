n = int(input())

last_left_index = 0
last_right_index = 0

result = 0
for i in range(n):
    index, hand = input().split()
    index = int(index)

    if hand == 'L':
        if last_left_index == 0:
            last_left_index = index
            continue
        else:
            result += abs(index - last_left_index)
            last_left_index = index
    else:
        if last_right_index == 0:
            last_right_index = index
            continue
        else:
            result += abs(index - last_right_index)
            last_right_index = index

print(result)