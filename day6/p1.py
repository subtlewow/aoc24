from pathlib import Path

def find_starting(arr: list[list[str]]):
    for i in range(len(arr)):
        if '^' in arr[i]:
            return (i, arr[i].index('^'))

def validate_bounds(i, j, n, m):
    return 0 <= i < n and 0 <= j < m

base_path = Path(__file__).parent

with open(base_path / "sample.txt") as f:
    grid = [list(line.strip('\n')) for line in f]

n, m = len(grid), len(grid[0])
x, y = find_starting(grid)

grid[x][y] = 'X'

directions = [(-1,0), (0,1), (1,0), (0,-1)]

k = 0
in_bounds = True
valid_count = 0

while in_bounds:
    k = k % len(directions) # handling overflow
    dx, dy = directions[k]

    while x < n and y < m:
        if validate_bounds(x+dx, y+dy, n, m) and grid[x+dx][y+dy] == '#':
            k += 1
            break

        x = x + dx
        y = y + dy

        if not validate_bounds(x, y, n, m):
            in_bounds = False
            break

        grid[x][y] = 'X'

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'X':
            valid_count += 1

print(valid_count)
