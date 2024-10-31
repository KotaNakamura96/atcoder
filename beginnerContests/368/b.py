def count_positive_integer(numbers):
    positive_integer_count = 0
    for number in numbers:
        if number > 0:
            positive_integer_count += 1

    return positive_integer_count

n = int(input())
numbers = [int(i) for i in input().split()]

positive_integer_count = count_positive_integer(numbers)
result = 0

while positive_integer_count > 1:
    numbers.sort(reverse=True)
    numbers[0] -= 1
    numbers[1] -= 1
    positive_integer_count = count_positive_integer(numbers)
    result += 1

print(result)