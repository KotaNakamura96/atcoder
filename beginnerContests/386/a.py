from collections import Counter

numbers = [int(i) for i in input().split()]
duplicate_elements = [item for item, count in Counter(numbers).items() if count > 1]

duplicate_count = len(duplicate_elements)
if duplicate_count == 0:
    print('No')
elif duplicate_count == 1:
    number_count = numbers.count(duplicate_elements[0])
    if number_count == 3:
        print('Yes')
    else:
        print('No')
elif duplicate_count == 2:
    first_number_count = numbers.count(duplicate_elements[0])
    second_number_count = numbers.count(duplicate_elements[1])
    if first_number_count == 2 and second_number_count == 2:
        print('Yes')
    else:
        print('No')
else:
    print('No')
