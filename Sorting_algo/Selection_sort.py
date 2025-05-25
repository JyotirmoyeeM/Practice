"""
Selection Sort is a comparison-based sorting algorithm
where the smallest (or largest) element is repeatedly selected
  from the unsorted portion of the list 
    and placed at the beginning. 
    
This process continues until the entire list is sorted.
At each step, the algorithm selects the correct element and places it in its final position, reducing the size of the unsorted portion.
"""

def selection_sort(lst):
    size =len(lst)
    for i in range(size):
        min_index = i
        for j in range(i+1, size):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index],  = lst[min_index], lst[i]
    return lst
    
data= [1,2,5,3,7,6]

print(selection_sort(data))
