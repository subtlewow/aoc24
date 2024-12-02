from sys import stdin
from collections import Counter

x = [list(map(int, line.split())) for line in stdin]
first_elements = sorted(sublist[0] for sublist in x)
second_elements = sorted(sublist[1] for sublist in x)

counter = Counter(second_elements)

dist = sum([x1 * counter[x1] for x1 in first_elements])
print(dist)
