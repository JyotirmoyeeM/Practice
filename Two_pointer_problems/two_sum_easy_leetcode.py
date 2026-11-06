"""Find two input indices whose values add up to a target.

Problem: Return original indices of two values that sum to the target.
Approach: Sort value-index pairs, then scan inward with two pointers.
Complexity: O(n log n) time and O(n) extra space.
Assumptions: Return any one matching pair; values need not be pre-sorted.
"""


def pair_sum(arr, x):
    """Return a pair of zero-based input indices, or ``[]`` if none exists.

    Values are sorted together with their original indices, so ``arr`` is not
    modified. Time: O(n log n). Extra space: O(n).
    """
    values = sorted((num, index) for index, num in enumerate(arr))
    low, high = 0, len(values) - 1

    while low < high:
        total = values[low][0] + values[high][0]
        if total == x:
            return values[low][1], values[high][1]
        if total > x:
            high -= 1
        else:
            low += 1
    return []


if __name__ == "__main__":
    print(pair_sum([1, 3, 6, 2, 5, 4, 3, 2, 4], 7))
