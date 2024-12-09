from pathlib import Path

base_path = Path(__file__).parent

def is_valid_point(x: int, y: int, n: int, m: int):
    '''
    Checks if point (x,y) is within valid bounds.

    Args:
    - n: rows (int)
    - m: cols (int)
    '''

    return 0 <= x < n and 0 <= y < m

def upper_left_to_lower_diagonal(grid: list[str], posX: int, posY: int):
    combinations = [-1, 0, 1]
    temp = []

    for i in combinations:
        new_x = posX+i
        new_y = posY+i

        if not is_valid_point(new_x, new_y, len(grid), len(grid[0])):
            return ""

        temp.append(grid[new_x][new_y])

    print("left: ", temp, (new_x, new_y))

    return "".join(temp)

def lower_left_to_upper_diagonal(grid: list[str], posX: int, posY: int):
    combinations = [1, 0, -1]
    temp = []

    for i in combinations:
        new_x = posX+i
        new_y = posY-i

        if not is_valid_point(new_x, new_y, len(grid), len(grid[0])):
            return ""

        temp.append(grid[new_x][new_y])

    print("right: ", temp, (new_x, new_y))

    return "".join(temp)

def compare_diagonals(grid: list[str], x: int, y: int):
    rows, cols = len(grid), len(grid[0])
    count = 0

    if not is_valid_point(x, y, rows, cols):
        return False

    left = upper_left_to_lower_diagonal(grid, x, y)
    right = lower_left_to_upper_diagonal(grid, x, y)

    if len(left) == 3 and len(right) == 3 and left in ['SAM', 'MAS'] and right in ['SAM', 'MAS']:
        if left == right:
            count += 1

        elif left == right[::-1]:
            count += 1

        elif left[::-1] == right:
            count += 1

        elif left[::-1] == right[::-1]:
            count += 1

    return count


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

def grid_search(grid: list[str]):
    rows, cols = len(grid), len(grid[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            count += check_for_xmas_directions(grid, i, j)

    return count


with open(base_path / "sample.txt") as f:
    grid = [line.strip('\n') for line in f]
    x = grid_search(grid)
    print(f"XMAS appears: {x} times")
