"""
write a program for the problem: You have a list of numbers, and you want to find pairs of numbers that add up to a specific target value.
For example, if your numbers are [1, 8, 3, 6, 5, 7] and your target is 10, the pairs would be (3,7) and (5,5).

"""

#Solution

#psudo_code
"""
Solving using 2 pointer method
  Initialize the function with an array and a target:
      initialise count(number of pairs with summation equals to target)
      Sort the array
      left = 0 index
      right = length(arr) - 1 index
      pair = [] Initialize an empty list to store all combinations

      First loop where left < right:
        total = arr[left] + arr[right]
        2nd loop if total == target:
          found the pair
          add the pair to pair list
          increase count
          increase left index
          decrease right index
        elif total > target:
          didnt find pair
          decrease right index
        else:
          increase left index
      return (count, pair)
          
      
"""

def pair_sum(arr, x):
  count = 0
  pair = []
  left = 0
  right = len(arr) - 1
  arr.sort()
  while left < right:
    total = arr[left] + arr[right]
    if total == x:
      #pair found
      count += 1
      pair.append([arr[left] + arr[right]])
      left += 1
      right -= 1
    elif total > x:
      right -= 1
    else:
      left += 1
  return (count, pair)


pair_sum([1,3,6,2,5,4,3,2,4], 7)
print(pair_sum([1,3,6,2,5,4,3,2,4], 7))
      
      
