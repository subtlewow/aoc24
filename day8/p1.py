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

def detect_pairs(pair1, pair2):
    return ord(pair1) == ord(pair2)


def calculate_distance(i: int, j: int, k: int, l: int) -> tuple[int, int]:
    return (abs(k - i), abs(l - j))


def check_diagonals(i: int, j: int, lines: list[list[str]]):
    n, m = len(lines), len(lines[0])
    ans = 0

    x = 1
    coords = []
    adjacent_pairs = []

    if not is_antenna(lines[i][j]):
        return 0

    antenna = lines[i][j]

    while i + x < n:
        curr_row = lines[i + x]

        if antenna and antenna in curr_row:
            dist_x, dist_y = calculate_distance(i, j, i + x, curr_row.index(antenna))
            adjacent_pairs.append((i, j))
            adjacent_pairs.append((i + x, curr_row.index(antenna)))
            coords.append((dist_x, dist_y))

        x += 1

    while coords:
        dx, dy = coords.pop(0)

        x1, y1 = adjacent_pairs.pop(0)
        x2, y2 = adjacent_pairs.pop(0)

        # top right
        if is_valid(x1+dx, y1+dy, n, m) and detect_pairs(lines[x1][y1], lines[x1+dx][y1+dy]):
            # top left
            if is_valid(x1-dx, y1-dy, n, m) and lines[x1-dx][y1-dy] != '#':
                if lines[x1-dx][y1-dy] == '.':
                    lines[x1-dx][y1-dy] = '#'
                ans += 1

        if is_valid(x2-dx, y2-dy, n, m) and detect_pairs(lines[x2][y2], lines[x2-dx][y2-dy]):
            # bottom right
            if is_valid(x2+dx, y2+dy, n, m) and lines[x2+dx][y2+dy] != '#':
                if lines[x2+dx][y2+dy] == '.':
                    lines[x2+dx][y2+dy] = '#'
                ans += 1

        if is_valid(x1+dx, y1-dy, n, m) and detect_pairs(lines[x1][y1], lines[x1+dx][y1-dy]):
            # top right
            if is_valid(x1-dx, y1+dy, n, m) and lines[x1-dx][y1+dy] != '#':
                if lines[x1-dx][y1+dy] == '.':
                    lines[x1-dx][y1+dy] = '#'

                ans += 1

        if is_valid(x2-dx, y2+dy, n, m) and detect_pairs(lines[x2][y2], lines[x2-dx][y2+dy]):
            # bottom left
            if is_valid(x2+dx, y2-dy, n, m) and lines[x2+dx][y2-dy] != '#':
                if lines[x2+dx][y2-dy] == '.':
                    lines[x2+dx][y2-dy] = '#'
                ans += 1
    print(lines)

    return ans

ans = 0
for i in range(n):
    for j in range(m):
        ans += check_diagonals(i, j, lines)

print(ans)
