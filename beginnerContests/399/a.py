def calculate_difference(s: str, t: str) -> int:
    if s == t:
        return 0
    
    return sum(char_s != char_t for char_s, char_t in zip(s, t))

n = int(input())
s = input()
t = input()

result = calculate_difference(s, t)
print(result)
