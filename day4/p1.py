from pathlib import Path

base_path = Path(__file__).parent
print(base_path)

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
    if grid[x][y] == '.':
        return

    directions = [(0, 1), (0, -1), (1,0), (-1,0), (1,1), (-1,-1)]
    rows, cols = len(grid), len(grid[0])
    final = 0

    print(f"x, y => {(x,y)}")

    for xi, yj in directions:
        temp = []

        for j in range(4):
            new_x = x + (xi * j)
            new_y = y + (yj * j)

            if not is_valid_point(new_x, new_y, rows, cols) or grid[new_x][new_y] == '.':
                break

            print(new_x, new_y, grid[new_x][new_y])
            temp.append(grid[new_x][new_y])

        print("")
        if len(temp) == 4 and "".join(temp) == 'XMAS':
            final += 1

        # print(f"Found XMAS at ({x},{y}) in direction ({xi},{yj})", final)

    return final

def grid_search(grid: list[str]):
    # query = "XMAS"

    rows, cols = len(grid), len(grid[0])
    count = 0

    for i in range(rows):
        for j in range(cols):
            count += check_for_xmas_directions(grid, i, j)

    return count


with open(base_path / "sample.txt") as f:
    grid = [line.strip('\n') for line in f]
    x = grid_search(grid)
    print(x)
