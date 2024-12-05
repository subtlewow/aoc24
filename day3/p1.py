import re
from pathlib import Path

base_path = Path(__file__).parent
final = 0
with open(base_path / "sample.txt") as f:
    pattern = r"mul\(\d{1,3},\d{1,3}\)" # matches cases of mul(a, b)

    for line in f:
        lines = re.findall(pattern, line)

        for line in lines:
            integers = list(map(int, re.findall(r"\d+", line)))
            print(integers)
            final += integers[0] * integers[1]

print(final)
