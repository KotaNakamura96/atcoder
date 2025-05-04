from typing import List

def rotate(grid: List[str]) -> List[str]:
    rotated_grid = ["".join(row[::-1]) for row in zip(*grid)]
    return rotated_grid

def calculate_diff(grid1: List[str], grid2: List[str]) -> int:
    n = len(grid1)
    diff_count = 0
    for r in range(n):
        for c in range(n):
            if grid1[r][c] != grid2[r][c]:
                diff_count += 1
    return diff_count

def read_grid(n: int) -> List[str]:
    grid = []
    for _ in range(n):
        row = input()
        grid.append(row)
    return grid

def main() -> None:
    n = int(input())
    s_grid = read_grid(n)
    t_grid = read_grid(n)

    min_cost = float('inf')
    current_s_grid = s_grid

    for rotation_count in range(4):
        diff = calculate_diff(current_s_grid, t_grid)
        total_cost = rotation_count + diff
        min_cost = min(min_cost, total_cost)

        if rotation_count < 3:
            current_s_grid = rotate(current_s_grid)

    print(min_cost)

if __name__ == "__main__":
    main()