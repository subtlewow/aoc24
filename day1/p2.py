from sys import stdin
from typing import Dict

x = [list(map(int, line.split())) for line in stdin]
left = sorted(elem[0] for elem in x)

right_count: Dict[int, int] = {}

for elem in x:
    right_count[elem[1]] = right_count.get(elem[1], 0) + 1

similarity = sum([x1 * right_count[x1] for x1 in left if x1 in right_count])
print(similarity)
