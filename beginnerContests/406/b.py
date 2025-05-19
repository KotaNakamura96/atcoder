n, k = map(int, input().split())
operation_counts = [int(i) for i in input().split()]

result = 1
for i in range(len(operation_counts)):
    result *= operation_counts[i]

    if k < len(str(result)):
        result = 1

print(result)