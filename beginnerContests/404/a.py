import string

def find_smallest_missing_char(text: str) -> str:
    present_chars = set(text)
    for char in string.ascii_lowercase:
        if char not in present_chars:
            return char

    raise ValueError("Input string contains all lowercase letters 'a' through 'z'.")

def main() -> None:
    s = input()
    result = find_smallest_missing_char(s)
    print(result)

if __name__ == "__main__":
    main()
