from typing import Tuple
from collections import Counter


def p2(data: Tuple[list[int], list[int]]) -> int:
    """
        Given two lists x, y of equal length n,
        calculate the total similarity score where each score is calculated by
        multiplying each number in x by the frequency of its occurrence in y.
    """
    left, right = data
    right_freq = Counter(right)
    similarity = sum([x1 * right_freq[x1] for x1 in left if x1 in right_freq])
    return similarity
