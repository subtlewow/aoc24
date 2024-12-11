from pathlib import Path
from collections import defaultdict

base_path = Path(__file__).parent

ordering_rules = []
page_numbers = []
blank = False

def is_subset(subarr: list[int], arr: list[int]):
    return all(x in arr for x in subarr)

def find_middle(arr: list[int]):
    return arr[len(arr) // 2]     # guaranteed to be odd length

with open(base_path / "sample.txt") as f:
    for line in f:
        if line == '\n':
            blank = True
            continue

        if blank:
            page_numbers.append(line)
        else:
            ordering_rules.append(line)

parsed_int_ordering_rules = [list(map(int, rule.strip('\n').split('|'))) for rule in ordering_rules]
parsed_page_numbers = [list(map(int, line.strip('\n').split(','))) for line in page_numbers]

# print(parsed_int_ordering_rules)

k, v = zip(*parsed_int_ordering_rules)

# 47|53 means "if update contains both 47 and 53, then 47 must come before 53"
rules = defaultdict(list)
for a, b in parsed_int_ordering_rules:
    rules[a].append(b)

valid = []

for update in parsed_page_numbers:
    count = 0

    for i, page_number in enumerate(update):
        subarr = update[i+1:] if i+1 < len(update) else []
        arr = rules[page_number]

        if is_subset(subarr, arr):
            count += 1
        else:
            break

    if count == len(update):
        valid.append(update)

ans = 0
for arr in valid:
    ans += find_middle(arr)

print(f"Sum of middle-page numbers: {ans}")
