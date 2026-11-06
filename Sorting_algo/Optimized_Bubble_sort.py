"""Optimized ascending bubble sort.

Problem: Sort a list in ascending order.
Approach: Swap out-of-order neighbors; after each pass, skip the sorted tail.
Complexity: O(n^2) worst-case time, O(n) best-case time, O(1) extra space.
Assumptions: The list contains mutually comparable values.
"""


def bubble_sort(lst):
    """Sort ``lst`` in place and return it.

    Time: O(n^2) worst case, O(n) best case. Extra space: O(1).
    """
    size = len(lst)
    for i in range(size):
        swapped = False
        for j in range(size - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break
    return lst


if __name__ == "__main__":
    data = [9, 8, 5, 4, 3, 2]
    print(bubble_sort(data))
