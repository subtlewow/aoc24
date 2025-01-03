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
    if grid[x][y] == '.':
        return 0

    directions = [(0, 1), (0, -1), (1,0), (-1,0), (1,1), (-1,-1), (-1,1), (1,-1)]
    rows, cols = len(grid), len(grid[0])
    final = 0

    for xi, yj in directions:
        temp = []
        for j in range(4):
            new_x = x + (xi * j)
            new_y = y + (yj * j)

            if not is_valid_point(new_x, new_y, rows, cols) or grid[new_x][new_y] == '.':
                break

            temp.append(grid[new_x][new_y])

        if len(temp) == 4 and "".join(temp) == 'XMAS':
            final += 1

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
