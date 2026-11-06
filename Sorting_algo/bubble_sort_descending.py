"""Descending bubble sort.

Problem: Sort a list in descending order.
Approach: Swap adjacent values when the left value is smaller.
Complexity: O(n^2) time and O(1) extra space.
Assumptions: The list contains mutually comparable values.
"""


def bubble_sort(lst):
    """Sort ``lst`` in place and return it.

    Time: O(n^2). Extra space: O(1).
    """
    size = len(lst)
    for i in range(size):
        for j in range(size - 1 - i):
            if lst[j] < lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


if __name__ == "__main__":
    data = list(map(int, input("Enter numbers separated by spaces: ").split()))
    print(bubble_sort(data))
