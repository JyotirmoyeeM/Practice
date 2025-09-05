#check palindrome usiing 2 pointers
"""
(

---
Hi, so life happened.
By that, I mean I gave an interview at Mphasis. The interviewer spoke with me for about an hour — which is generally a good sign. It usually means they’re genuinely interested, trying to gauge how you’d fit into the team, what responsibilities you could take on, and where your current strengths lie.

I was asked to solve a few coding problems — which I did — but what caught me off guard was the emphasis on pseudocode.
The interviewer was more interested in how I approached the problem, how I thought through it step by step, and whether I could explain that logic in a clear and structured way.

That’s where I stumbled.
I could write the code, but I wasn’t able to communicate the underlying logic effectively in pseudocode.

So here’s a lesson for all of us — learn to write pseudocode as well, folks.
It’s not just about solving problems, but showing how you think through them.
---
)
psudo code:
  Initialize two pointers:
    lo at the start (0)
    hi at the end (len(array) - 1)
  Loop while lo <= hi:
    Compare the elements at lo and hi.
        If they are not equal, return False — it’s not a palindrome.
                If they are equal, move the pointers:
        lo moves forward (lo += 1)
        hi moves backward (hi -= 1)
  If loop completes without mismatches, return True.
"""
def check_palindrome(nums):
    lo = 0
    hi = len(nums) - 1
    while lo <= hi:
        if nums[lo] != nums[hi]:
            return False
        lo += 1
        hi -= 1
    return True
nums = [1,2,3,1]
print(check_palindrome(nums))
