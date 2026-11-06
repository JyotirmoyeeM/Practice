"""Ascending selection sort.

Problem: Sort a list in ascending order.
Approach: Find the smallest value in the unsorted suffix and move it forward.
Complexity: O(n^2) time and O(1) extra space.
Assumptions: The list contains mutually comparable values.
"""


def selection_sort(lst):
    """Sort ``lst`` in place and return it.

    Time: O(n^2). Extra space: O(1).
    """
    size = len(lst)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


if __name__ == "__main__":
    data = [1, 2, 5, 3, 7, 6]
    print(selection_sort(data))
