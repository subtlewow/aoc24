from pathlib import Path
from collections import defaultdict

base_path = Path(__file__).parent

ordering_rules = []
page_numbers = []
update = False

with open(base_path / "sample.txt") as f:
    for line in f:
        if line == '\n':
            update = True
            continue

        if update:
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

# print(sorted(parsed_int_ordering_rules))
print(rules)
print(parsed_page_numbers)

valid = []


for update in parsed_page_numbers:
    is_valid = True

    for i, page_number in enumerate(update):
        if i+1 < len(update) and page_number in rules:
            next_number = update[i+1]
            order = rules[page_number]

            if next_number not in order:
                is_valid = False
                break

    if is_valid:
        valid.append(update)


print(valid)
