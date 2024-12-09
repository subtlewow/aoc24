from pathlib import Path

base_path = Path(__file__).parent

def is_valid_point(x: int, y: int, n: int, m: int) -> bool:
    '''
    Checks if point (x,y) is within valid bounds.

    Args:
    - n: rows (int)
    - m: cols (int)
    '''

    return 0 <= x < n and 0 <= y < m

def is_valid_mas_string(s: str) -> bool:
    return len(s) == 3 and s in ['SAM', 'MAS']

def get_diagonal_string(grid: list[str], posX: int, posY: int, pos: int = 1) -> str:
    combinations = [-1, 0, 1]
    temp = []

    for i in combinations:
        new_x = posX+(i*pos)
        new_y = posY+i

        if not is_valid_point(new_x, new_y, len(grid), len(grid[0])):
            return ""

        temp.append(grid[new_x][new_y])

    return "".join(temp)

def compare_diagonals(grid: list[str], x: int, y: int) -> int:
    right = get_diagonal_string(grid, x, y)
    left = get_diagonal_string(grid, x, y, -1)

    if not (is_valid_mas_string(left) and  is_valid_mas_string(right)):
        return 0

    is_matching_pattern = (
        left == right or # left == right and left[::-1] == right[::-1] are equivalent
        left == right[::-1] # left == right[::-1] and right == left[::-1] are equivalent
    )

    return 1 if is_matching_pattern else 0

def check_for_xmas_directions(grid: list[str], x: int, y: int):
    '''
        {
            - only perform search if X from XMAS is found, then build strings, append to list then .join().

            forward: (x, y+4)
            backward: (x, y-4)
            down: (x+4, y)
            up: (x-4, y)
            diag_bottom_right: (x+4, y+4)
            diag_top_left: (x-4, y-4)
            diag_top_right: (x-4, y+4)
            diag_bottom_left: (x+4, y-4)
        }

    '''
    final = 0

    if grid[x][y] == 'A':
        final = compare_diagonals(grid, x, y)

    return final

def grid_search(grid: list[str]) -> int:
    rows, cols = len(grid), len(grid[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            count += check_for_xmas_directions(grid, i, j)

    return count


with open(base_path / "sample.txt") as f:
    grid = [line.strip('\n') for line in f]
    x = grid_search(grid)
    print(f"X-MAS appears: {x} times")
