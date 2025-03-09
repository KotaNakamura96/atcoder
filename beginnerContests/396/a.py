n = int(input())
numbers = [int(i) for i in input().split()]

last_num = 0
count = 1
result = 'No'
for i in range(n):
    if i == 0:
        last_num = numbers[i]
        continue

    if last_num == numbers[i]:
        count += 1
        if count == 3:
            result = 'Yes'
            break
    else:
        count = 1

    last_num = numbers[i]

print(result)
