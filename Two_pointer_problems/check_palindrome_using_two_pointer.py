"""Check whether a sequence reads the same forwards and backwards.

Problem: Determine whether a sequence is a palindrome.
Approach: Compare values at the ends and move both pointers toward the center.
Complexity: O(n) time and O(1) extra space.
Assumptions: Values support equality comparison; empty sequences are palindromes.
"""


def check_palindrome(nums):
    """Return whether ``nums`` is a palindrome using O(1) extra space.

    Time: O(n); empty sequences are palindromes.
    """
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        if nums[lo] != nums[hi]:
            return False
        lo += 1
        hi -= 1
    return True


if __name__ == "__main__":
    print(check_palindrome([1, 2, 3, 1]))
