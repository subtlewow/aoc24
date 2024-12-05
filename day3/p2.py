import re
from pathlib import Path

base_path = Path(__file__).parent

def calc_prod_sum(line: str):
    integers = list(map(int, re.findall(r"\d+", line)))
    return integers[0] * integers[1]

state = True
final = 0
with open(base_path / "sample.txt") as f:
    pattern = r"(?:do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))" # matches all mul(a,b) cases AND do(), don't() cases.

    for line in f:
        lines = re.findall(pattern, line)

        for line in lines:
            if line == 'do()':
                state = True
                continue
            elif line == "don't()":
                state = False

            if state:
                final += calc_prod_sum(line)

print(final)
