from pathlib import Path

base_path = Path(__file__).parent

with open(base_path / "sample.txt") as f:
    lines = [line.split(": ") for line in f]
    lines = [[test, numbers.strip("\n").split()] for test, numbers in lines]

a, b = zip(*lines)
test = list(map(int, a))
numbers = [list(map(int, line)) for line in b]


def mixture(arr: list[int], expected: int):
    n = len(arr)

    num_combinations = 2 ** (n - 1)
    k = 0

    while k < num_combinations:
        ans = arr[0]
        curr_combo = []

        # define the combination of operations
        temp = k
        for _ in range(n - 1):
            if temp % 2 == 0:
                curr_combo.append("+")
            else:
                curr_combo.append("x")
            temp //= 2

        # evaluate in order w/ operators
        for i in range(n - 1):
            if curr_combo[i] == "+":
                ans += arr[i + 1]
            else:
                ans *= arr[i + 1]

        if ans == expected:
            return True

        k += 1

    return False


real = []
m = len(test)
for i in range(m):
    expected = test[i]
    actual = 1
    res = 0

    if mixture(numbers[i], expected) or sum(numbers[i]) == expected:
        real.append(expected)

print(sum(real))
