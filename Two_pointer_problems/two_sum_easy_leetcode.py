"""
Two sum easy level from leetcode demands me to find the pairs from int array that sums to target, 
but when i return them , 
i should return the indices oof those two elemnt from array
"""

def pair_sum(arr, x):
  arr = [(num, indices) for indices, num in enumerate(arr)]
  arr.sort()
  
  low, high = 0, len(arr) - 1
  for _ in range(len(arr)):
    if low >= high:
      break
    total = arr[low][0] + arr[high][0]
    if total == x: #foundthem
      return(arr[low][1], arr[high][1])
    elif total > x:
      high -= 1
    else:
      low += 1
  return []


pair_sum([1,3,6,2,5,4,3,2,4], 7)
print(pair_sum([1,3,6,2,5,4,3,2,4], 7))  #outpur (0,2)
