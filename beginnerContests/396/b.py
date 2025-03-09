query_count = int(input())
numbers = [0] * 100

for i in range(query_count):
    query = [int(n) for n in input().split()]
    if query[0] == 1:
        x = query[1]
        numbers.append(x)

    else:
        removed_num = numbers.pop(-1)
        print(removed_num)
