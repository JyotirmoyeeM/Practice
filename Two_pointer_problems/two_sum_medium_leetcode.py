"""Two Sum II for an ascending, already-sorted input.

Problem: Find two positions in sorted input whose values sum to the target.
Approach: Move the left or right pointer according to whether the sum is low
or high; return both zero-based and one-based index pairs.
Complexity: O(n) time and O(1) extra space.
Assumptions: Input must be sorted in non-decreasing order.
"""


def pair_sum(arr, x):
    """Return ``(zero_based_indices, one_based_indices)`` for a matching pair.

    The input must be sorted in non-decreasing order. Raises ``ValueError`` if
    it is not sorted; returns ``[]`` when no pair is found. Time: O(n), extra
    space: O(1).
    """
    if any(arr[i] > arr[i + 1] for i in range(len(arr) - 1)):
        raise ValueError("arr must be sorted in non-decreasing order")

    low, high = 0, len(arr) - 1
    while low < high:
        total = arr[low] + arr[high]
        if total == x:
            return (low, high), (low + 1, high + 1)
        if total > x:
            high -= 1
        else:
            low += 1
    return []


if __name__ == "__main__":
    print(pair_sum([1, 2, 3, 4, 6], 7))
