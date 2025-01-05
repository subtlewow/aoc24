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

def validate_diagonal(x1: int, y1: int, x2: int, y2: int, dx: int, dy: int, n: int, m: int, lines: list[list[str]]) -> int:
    directions = [
        ((1,1), (-1,-1)), # UL to LR diagonal (adj. 1)
        ((-1,-1), (1,1)), # LR to UL diagonal (adj. 1)
        ((1,-1), (-1,1)), # LL to UR diagonal (adj. 2)
        ((-1,1), (1,-1))  # UR to LL diagonal (adj. 2)
    ]
    ans = 0

    for dir1, dir2 in directions:
        new_x1 = x1 + (dx * dir1[0])
        new_x2 = x2 + (dx * dir2[0])

        new_y1 = y1 + (dy * dir1[1])
        new_y2 = y2 + (dy * dir2[1])

        if is_valid(new_x1, new_y1, n, m) and detect_pairs(lines[x1][y1], lines[new_x1][new_y1]):
            new_x1 = x1 + (dx * dir2[0])
            new_y1 = y1 + (dy * dir2[1])

            if is_valid(new_x1, new_y1, n, m) and lines[new_x1][new_y1] != '#':
                if lines[new_x1][new_y1] == '.':
                    lines[new_x1][new_y1] = '#'
                ans += 1

        if is_valid(new_x2, new_y2, n, m) and detect_pairs(lines[x2][y2], lines[new_x2][new_y2]):
            new_x2 = x2 + (dx * dir1[0])
            new_y2 = y2 + (dy * dir1[1])

            if is_valid(new_x2, new_y2, n, m) and lines[new_x2][new_y2] != '#':
                if lines[new_x2][new_y2] == '.':
                    lines[new_x2][new_y2] = '#'
                ans += 1

    return ans



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

        ans += validate_diagonal(x1, y1, x2, y2, dx, dy, n, m, lines)

    return ans

ans = 0
for i in range(n):
    for j in range(m):
        ans += check_diagonals(i, j, lines)

print(f"Unique locations: {ans}")
