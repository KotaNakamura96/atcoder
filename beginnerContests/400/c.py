def count_valid_numbers(n: int):
    good_numbers = set()

    b = 1
    while b * b <= n:
        max_power = n // (b * b)

        if max_power < 2:
            b += 1
            continue

        max_a = max_power.bit_length() - 1

        for a in range(1, max_a + 1):
            num = (1 << a) * (b * b)
            if num <= n:
                good_numbers.add(num)

        b += 1

    return len(good_numbers)


n = int(input())
result = count_valid_numbers(n)
print(result)

