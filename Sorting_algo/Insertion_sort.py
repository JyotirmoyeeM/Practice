"""Ascending insertion sort.

Problem: Sort a list in ascending order.
Approach: Insert each next value into its position in the sorted prefix.
Complexity: O(n^2) worst-case time, O(n) best-case time, O(1) extra space.
Assumptions: The list contains mutually comparable values.
"""


def insertion_sort(arr):
    """Sort ``arr`` in place and return it.

    Time: O(n^2) worst case, O(n) best case. Extra space: O(1).
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    data = [5, 6, 4, 2, 1]
    print(insertion_sort(data))
