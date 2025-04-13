
"""
suppose we have to create the following dictionary from the list:
 {1: 1, 2: 4, 3: 9, 4: 16} 
 
 here,

The keys of the dictionary are the items of the list
Their corresponding values are the squares of the items.
"""

n=int(input())

numbers = [ i for i in range(1, n=1)]
print(numbers)

square_numbers ={}

for i in numbers:
  square_numbers[i] = i**2
print(square_numbers)
