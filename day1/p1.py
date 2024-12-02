from sys import stdin

x = [list(map(int, line.split())) for line in stdin]
left = sorted(elem[0] for elem in x)
right = sorted(elem[1] for elem in x)
x = list(map(list, zip(left, right)))
dist = sum([abs(x1 - x2) for x1, x2 in x])
print(dist)
