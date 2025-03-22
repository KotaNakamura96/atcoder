from typing import Dict, List, Set

def count_numbers(numbers: List[int]) -> Dict[int, int]:
    number_counts: Dict[int, int] = {}
    for n in numbers:
        number_counts[n] = number_counts.get(n, 0) + 1

    return number_counts

def can_make_three_card_and_pair(number_counts: Dict[int, int]) -> bool:
    for num_x, count_x in number_counts.items():
        if count_x >= 3:
            for num_y, count_y in number_counts.items():
                if num_x != num_y and count_y >= 2:
                    return True
    
    return False

def can_make_four_card_and_pair(number_counts: Dict[int, int]) -> bool:
    for num_x, count_x in number_counts.items():
        if count_x >= 4:
            for num_y in number_counts:
                if num_x != num_y:
                    return True
    return False

def can_make_full_house(number_counts: Dict[int, int]) -> bool:
    return can_make_three_card_and_pair(number_counts) or can_make_four_card_and_pair(number_counts)
    

def main() -> None:
    numbers: List[int] = [int(i) for i in input().split()]
    number_counts: Dict[int, int] = count_numbers(numbers)
    result: bool = can_make_full_house(number_counts)
    print('Yes' if result else 'No')

if __name__ == '__main__':
    main()
