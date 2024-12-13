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
start_x, start_y = find_starting(grid)

grid[start_x][start_y] = 'X'

directions = [(-1,0), (0,1), (1,0), (0,-1)]

def generate_grid(start_x, start_y, grid):
    k = 0
    x, y = start_x, start_y

    # track (x, y, current direction) for every point visited.
    visited_states = set()
    visited_states.add((x,y,k))

    while True:
        dx, dy = directions[k % len(directions)]

        next_x = x + dx
        next_y = y + dy

        if not validate_bounds(next_x, next_y, n, m):
            break

        if grid[next_x][next_y] == '#':
            k = (k+1) % len(directions)

            if (x,y,k) in visited_states:
                return True
        else:
            x, y = next_x, next_y

            if (x,y,k) in visited_states:
                return True

            visited_states.add((x,y,k))
            grid[x][y] = 'X'

    return grid

grid = generate_grid(start_x, start_y, grid)

valid_count = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 'X':
            valid_count += 1

print(valid_count)
