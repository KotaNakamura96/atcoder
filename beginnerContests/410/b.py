n, q = map(int, input().split())
boxes = {}
for i in range(n):
    boxes[i + 1] = 0

numbers = list(map(int, input().split()))
result = []
for i in range(len(numbers)):
    if numbers[i] >= 1:
        boxes[numbers[i]] += 1
        result.append(numbers[i])
    else:
        min_box_key = min(boxes, key=boxes.get)
        boxes[min_box_key] += 1
        result.append(min_box_key)

print(*result)

