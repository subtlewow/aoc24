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

directions = [(-1,0), (0,1), (1,0), (0,-1)]

def simulate_grid(grid, start_x, start_y, obs_x, obs_y):
    test_grid = [row[:] for row in grid] # deepcopy of grid

    if test_grid[obs_x][obs_y] != '.' or (start_x == obs_x and start_y == obs_y):
        return False

    test_grid[obs_x][obs_y] = '#'

    return find_cycle(start_x, start_y, test_grid)

def find_cycle(start_x, start_y, grid):
    k = 0
    x, y = start_x, start_y

    # track (x, y, current direction) for every point visited.
    visited_states = set()

    while True:
        current_state = (x,y,k)
        if current_state in visited_states:
            return True

        visited_states.add(current_state)

        dx, dy = directions[k % len(directions)]

        next_x = x + dx
        next_y = y + dy

        if not validate_bounds(next_x, next_y, n, m):
            return False

        if grid[next_x][next_y] == '#':
            k = (k+1) % len(directions)
        else:
            x, y = next_x, next_y

        if len(visited_states) > n*m*len(directions):
            return False

positions = []
valid_count = 0
for i in range(n):
    for j in range(m):
        if simulate_grid(grid, start_x, start_y, i, j):
            positions.append((i, j))

print(f"Number of positions: {len(positions)}")
