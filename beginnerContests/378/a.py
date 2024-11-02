numbers = [int(i) for i in input().split()]

result = 0
for i in range(4):
    number_count = numbers.count(i + 1)
    if number_count >= 2 and number_count < 4:
        result += 1
    elif numbers.count(i + 1) == 4:
        result += 2

print(result)