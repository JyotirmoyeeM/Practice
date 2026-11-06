"""Find disjoint value pairs whose sum equals a target.

Problem: Find pairs of values that add up to a target.
Approach: Sort a copy, then move two pointers inward based on their sum.
Complexity: O(n log n) time and O(n) extra space.
Assumptions: Each input occurrence can be used once; duplicate values count
as separate occurrences.
"""


def pair_sum(arr, x):
    """Return ``(count, pairs)`` without modifying ``arr``.

    The result contains value pairs, not index pairs. Each input occurrence is
    used at most once. Sorting dominates the O(n log n) time; the sorted copy
    uses O(n) extra space.
    """
    values = sorted(arr)
    count = 0
    pairs = []
    left = 0
    right = len(values) - 1

    while left < right:
        total = values[left] + values[right]
        if total == x:
            pairs.append((values[left], values[right]))
            count += 1
            left += 1
            right -= 1
        elif total > x:
            right -= 1
        else:
            left += 1
    return count, pairs


if __name__ == "__main__":
    print(pair_sum([1, 3, 6, 2, 5, 4, 3, 2, 4], 7))
