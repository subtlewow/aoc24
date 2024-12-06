from typing import Tuple

def p1(data: Tuple[list[int], list[int]]) -> int:
    """
        Given two lists x, y of equal length n,
        find the total distance when elements are paired (xi, yi)
        after both lists are sorted in ascending order, such that 0 <= i < n.
    """
    left, right = data
    dist = sum([abs(right[i] - left[i]) for i in range(len(data[0]))])
    return dist
