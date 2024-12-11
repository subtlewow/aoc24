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

def swap(update, i, j):
    update[i], update[j] = update[j], update[i]

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

k, v = zip(*parsed_int_ordering_rules)

# 47|53 means "if update contains both 47 and 53, then 47 must come before 53"
rules = defaultdict(list)
for a, b in parsed_int_ordering_rules:
    rules[a].append(b)

print(rules)
invalid = []
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
    else:
        invalid.append(update)

# search through the keys, find where 75 exists, grab the key, then look for tha tkey in the update array.
# swap current position with 75.
# print(invalid)

final = []
for update in invalid:
    changed = True
    n = len(update)

    # keeps repeating until no more swaps (hence all rules satisfied)
    while changed:
        changed = False

        for i in range(n-1):
            curr = update[i]
            next_val = update[i+1]

            if curr in rules[next_val]:
                swap(update, i, i+1)
                changed = True
            elif next_val in rules[curr]:
                continue
            else:
                for before, after_list in rules.items():
                    if curr in after_list and before == next_val:
                        swap(update, i, i+1)
                        changed = True
                        break

    final.append(update)

# print(final)

ans = 0
for arr in final:
    ans += find_middle(arr)

print(f"Sum of middle-page numbers: {ans}")
