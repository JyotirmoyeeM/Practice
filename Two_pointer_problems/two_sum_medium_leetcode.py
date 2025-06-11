"""
So in this medium level leetcode problem of two sum, i have been asked for pair of element whos  summation equals to target
return their indices just one indices up 
like for expamle pair whos incides is (0,2) the output will be (1,3)
it is said they are already in sorted way
"""
def pair_sum(arr, x):
    low, high = 0, len(arr) - 1
    while low < high:
        total = arr[low] + arr[high]
        if total == x:
            
            return (low, high), (low + 1, high + 1)  # 1-based indexing
        elif total > x:
            high -= 1  # Move right pointer left to reduce sum
        else:
            low += 1  # Move left pointer right to increase sum
    return []  # No solution found


pair_sum([1,3,6,2,5,4,3,2,4], 7)
print(pair_sum([1,3,6,2,5,4,3,2,4], 7))
      
