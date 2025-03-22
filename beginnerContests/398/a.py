def generate(n: int) -> str:
    is_odd = n % 2 != 0
    half_num = n // 2
    result = ''
    
    for i in range(n):
        if is_odd:
            if i + 1 == half_num + 1:
                result += '='
            else:
                result += '-'
        else:
            if i + 1 == half_num or i + 1 == half_num + 1:
                result += '='
            else:
                result += '-'
                
    return result


def main() -> None:
    n = int(input())
    pattern = generate(n)
    print(pattern)


if __name__ == "__main__":
    main()