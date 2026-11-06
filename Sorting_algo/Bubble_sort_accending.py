"""Basic ascending bubble sort.

Problem: Sort a list in ascending order.
Approach: Swap out-of-order neighbors on each pass through the list.
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
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


if __name__ == "__main__":
    data = [1, 9, 2, 8, 3, 7]
    print(f"Unsorted list: {data}")
    print(f"Sorted list: {bubble_sort(data)}")
