import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from custom_types import InputData


def p1(data: InputData) -> int:
    """
        Given two lists x, y of equal length n,
        find the total distance when elements are paired (xi, yi)
        after both lists are sorted in ascending order, such that 0 <= i < n.
    """
    left, right = data
    dist = sum([abs(right[i] - left[i]) for i in range(len(data[0]))])
    return dist
