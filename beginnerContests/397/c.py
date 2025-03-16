number_length = int(input())
numbers = [int(i) for i in input().split()]

left_number_count = [0] * (number_length + 1)
left_numbers = set()
for i in range(number_length):
    left_numbers.add(numbers[i])
    left_number_count[i + 1] = len(left_numbers)

right_number_count = [0] * (number_length + 1)
right_numbers = set()
for i in range(number_length - 1, -1, -1):
    right_numbers.add(numbers[i])
    right_number_count[i] = len(right_numbers)

max_sum = 0
for i in range(1, number_length):
    max_sum = max(max_sum, left_number_count[i] + right_number_count[i])

print(max_sum)
