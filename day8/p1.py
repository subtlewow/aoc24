# check if any two antennas are twice as far away as one another ie. 2:1 ratio
# current[x-run][y+rise], current[x+run][y-rise] where (x-run, y-rise) are valid pts

# from (x,y) to n (rows) => check if same antenna exists in list[i], if so, calculate manhatten distance (l1 norm)

from pathlib import Path

base_path = Path(__file__).parent

with open(base_path / "sample.txt") as f:
    lines = [list(line.strip("\n")) for line in f]

n, m = len(lines), len(lines[0])


def is_valid(i: int, j: int, n: int, m: int) -> bool:
    """
    Checks if current coordinate is within bounds.

    Args:
        i (int): current x coordinate (row)
        j (int): current y coordinate (column)
        n (int): total number of rows
        m (int): total number of cols

    Returns:
        bool: True if valid, False otherwise
    """
    return 0 <= i < n and 0 <= j < m


def is_antenna(item: str) -> bool:
    """
    An Antenna is defined as a single lowercase, uppercase, or number.

    Args:
        item (str): _description_

    Returns:
        bool: True if valid, False otherwise
    """

    ascii_value = ord(item)
    return (
        (97 <= ascii_value <= 122)  # lowercase letters a-z
        or (65 <= ascii_value <= 90)  # uppercase letters A-Z
        or (48 <= ascii_value <= 57)  # numbers 0-9
    )


def calculate_distance(i: int, j: int, k: int, l: int, lines: list[list[str]]) -> tuple[int, int]:
    if i >= k:
        return (i - k, j - l)
    else:
        return (k - i, l - j)

def check_diagonals(i: int, j: int, lines: list[list[str]]):
    # adjacent_pair = False
    n, m = len(lines), len(lines[0])

    x = 1
    antenna = None
    coords = set()
    adjacent_pairs = set()

    if is_antenna(lines[i][j]) and is_valid(i, j, n, m):
        antenna = lines[i][j]

    if i + x < n:
        if antenna and antenna in lines[i + x]:
            dist_x, dist_y = calculate_distance(i, j, i + x, lines[i + x].index(antenna), lines)
            adjacent_pairs.add(((i, j), (i + x, lines[i + x].index(antenna))))
            coords.add((dist_x, dist_y))
        else:
            x += 1

    while coords:
        dx, dy = coords.pop()
        dx, dy = abs(dx), abs(dy)

        pair1, pair2 = adjacent_pairs.pop()
        x1, y1 = pair1
        x2, y2 = pair2

        if y2 > y1:
            # bottom right
            if is_valid(+dx, j+dy, n, m) and lines[i+dx][j+dy] == '.':
                lines[i+dx][j+dy] = '#'

        # upper right
        if is_valid(i-dx, j+dy, n, m) and lines[i-dx][j+dy] == '.':
            lines[i-dx][j+dy] = '#'

for i in range(n):
    for j in range(m):
        check_diagonals(i, j, lines)
