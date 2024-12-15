
# multiplication, iter w smallest difference
# sort the values on right

from pathlib import Path

base_path = Path(__file__).parent

with open(base_path / "sample.txt") as f:
    lines = [line.split(': ') for line in f]
    lines = [[test, numbers.strip('\n').split()] for test, numbers in lines]

a, b = zip(*lines)
test = list(map(int, a))
numbers = [list(map(int, line)) for line in b]

n = len(test)

real = []

for i in range(n):
    expected = test[i]
    actual = 1

    print(numbers[i])

    for num in numbers[i]:
        actual *= num

        if actual == expected:
            real.append(expected)
        elif actual > expected:




    print(real)
