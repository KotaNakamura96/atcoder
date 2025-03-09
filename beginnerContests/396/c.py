def calcurate_max_value(n, m, black_ball_values, white_ball_values):
    black_ball_values.sort(reverse=True)
    white_ball_values.sort(reverse=True)

    black_ball_value_cumulative_sums = [0] * (n + 1)
    white_ball_value_cumulative_sums = [0] * (m + 1)

    for i in range(n):
        black_ball_value_cumulative_sums[i + 1] = black_ball_value_cumulative_sums[i] + black_ball_values[i]

    for i in range(m):
        white_ball_value_cumulative_sums[i + 1] = white_ball_value_cumulative_sums[i] + white_ball_values[i]

    max_white_cumulative_sums = [0] * (m + 1)
    for i in range(1, m + 1):
        max_white_cumulative_sums[i] = max(max_white_cumulative_sums[i - 1], white_ball_value_cumulative_sums[i])

    max_value = 0

    for i in range(n + 1):
        min_white = min(i, m)
        value = black_ball_value_cumulative_sums[i] + max_white_cumulative_sums[min_white]
        max_value = max(max_value, value)

    return max_value

n, m = map(int, input().split())
black_ball_values = [int(i) for i in input().split()]
white_ball_values = [int(i) for i in input().split()]

print(calcurate_max_value(n, m, black_ball_values, white_ball_values))
