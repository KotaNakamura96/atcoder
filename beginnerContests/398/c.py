from typing import List, Dict, Tuple, Optional

def read_input() -> Tuple[int, List[int]]:
    n = int(input())
    having_numbers = [int(i) for i in input().split()]
    
    return n, having_numbers

def make_number_to_persons(n: int, having_numbers: List[int]) -> Dict[int, List[int]]:
    number_to_persons: Dict[int, List[int]] = {}
    for i in range(n):
        person_num = i + 1
        number = having_numbers[i]
        if number not in number_to_persons:
            number_to_persons[number] = []

        number_to_persons[number].append(person_num)
    
    return number_to_persons

def find_valid_persons(number_to_persons: Dict[int, List[int]]) -> List[Tuple[int, int]]:
    valid_persons: List[Tuple[int, int]] = []
    for number, persons in number_to_persons.items():
        if len(persons) == 1:
            valid_persons.append((number, persons[0]))

    return valid_persons

def find_max_number_person(valid_persons: List[Tuple[int, int]]) -> int:
    if not valid_persons:
        return -1
    
    valid_persons.sort(reverse=True)

    return valid_persons[0][1]

def main() -> None:
    n, having_numbers = read_input()
    number_to_persons = make_number_to_persons(n, having_numbers)
    valid_persons = find_valid_persons(number_to_persons)
    result = find_max_number_person(valid_persons)
    print(result)

if __name__ == '__main__':
    main()