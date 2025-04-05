def calculate_sum(n:int, m:int) -> int:
    max_value = 10 ** 9
    
    if n == 1:
        return m + 1
    
    if n == 0:
        return 1 if m == 0 else 2

    result = 0
    current_power = 1

    for i in range(m + 1):
        result += current_power
        if result > max_value:
            return "inf"
        
        if i < m:
            current_power *= n
            if current_power > max_value and i < m:
                return "inf"
            
    return result

n, m = map(int, input().split())
result = calculate_sum(n, m)
print(result)
