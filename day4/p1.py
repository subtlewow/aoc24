from pathlib import Path

base_path = Path(__file__).parent

def is_valid_point(x: int, y: int, n: int, m: int):
    """
    Checks if point (x,y) is within valid bounds.

    Args:
    - n: rows (int)
    - m: cols (int)
    """

    return 0 <= x < n and 0 <= y < m

def check_for_xmas_directions(grid: list[str], x: int, y: int):
    '''
        {
            - only perform search if X from XMAS is found, then build strings, append to list then .join().
            - x is inclusive so itll be x+3 instead of x+4

            forward: (x, y+4)
            backward: (x, y-4)
            down: (x+4, y)
            up: (x-4, y)
            diag_left_to_right: (x+4, y+4)
            diag_right_to_left: (x-4, y-4)
        }

    '''
    directions = [(1, 4), (1,-4), (3,1), (-3,1), (3,4), (-3,-4)]
    final = 0

    for xi, yj in directions:
        temp = []
        if grid[x][y] == 'X':
            for j in range(yj):
                temp.append(grid[x][y+j])

            if "".join(temp) == 'XMAS':
                final += 1


def grid_search(grid: list[str]):
    # query = "XMAS"

    rows, cols = len(grid), len(grid[0])

    for i in range(rows):
        for j in range(cols):
            check_for_xmas_directions(grid, i, j)

    return 0


with open(base_path / "sample.txt") as f:
    grid = [line.strip('\n') for line in f]

    x = grid_search(grid)
