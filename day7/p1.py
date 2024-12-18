from pathlib import Path

base_path = Path(__file__).parent

with open(base_path / "sample.txt") as f:
    lines = [line.split(": ") for line in f]
    lines = [[test, numbers.strip("\n").split()] for test, numbers in lines]

a, b = zip(*lines)
test = list(map(int, a))
numbers = [list(map(int, line)) for line in b]


def mixture(arr: list[int], expected: int) -> bool:
    n = len(arr)

    num_combinations = 2 ** (n - 1)
    k = 0

    while k < num_combinations:
        ans = arr[0]
        curr_combo = []

        # define the combination of operations
        temp = k
        for i in range(n - 1):
            if temp % 2 == 0:
                curr_combo.append("+")
            else:
                curr_combo.append("x")
            temp //= 2

        # evaluate in order w/ operators
        str_ans = ""
        str_expected = str(expected)
        for i in range(n - 1):
            str_ans += str(ans)

            if curr_combo[i] == "+":
                ans += arr[i + 1]
            else:
                ans *= arr[i + 1]

            if str_ans == str_expected:
                return True

        print(ans)

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

    if mixture(numbers[i], expected):
        real.append(expected)

print(sum(real))
